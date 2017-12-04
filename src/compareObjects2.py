import numpy as np
import cv2
from matplotlib import pyplot as plt

def compareObjects2(imagenBase, imagenBuscar):

    CONCORDANCIA_MINIMA = 10
    imagenCL1 = cv2.imread('BaseDatos/'+imagenBase+'.png') # imagen base
    imagenCL2 = cv2.imread('BaseDatos/'+imagenBuscar+'.png') # imagen a buscar
    cv2.imshow('Imagen1', imagenCL1)
    cv2.imshow('Imagen2', imagenCL2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    imagen1 = cv2.cvtColor(imagenCL1, cv2.COLOR_BGR2GRAY)
    imagen2 = cv2.cvtColor(imagenCL2, cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()

    puntos1, descripcion1 = sift.detectAndCompute(imagen1, None)
    puntos2, descripcion2 = sift.detectAndCompute(imagen2, None)

    FLANN_INDEX_KDTREE = 0
    indices_parametros = dict(algorithm = FLANN_INDEX_KDTREE, trees = 8)
    busquedas_recursivas = dict(checks = 100)

    flann = cv2.FlannBasedMatcher(indices_parametros, busquedas_recursivas)

    aciertos = flann.knnMatch(descripcion1, descripcion2, k=2)

    aciertos_validos = []
    for m,n in aciertos:
        if m.distance < 0.7*n.distance:
            aciertos_validos.append(m)
    if len(aciertos_validos)>CONCORDANCIA_MINIMA:
        origen_pto = np.float32([puntos1[m.queryIdx].pt for m in aciertos_validos]).reshape(-1, 1, 2)
        destino_pto = np.float32([puntos2[m.trainIdx].pt for m in aciertos_validos]).reshape(-1, 1, 2)

        M, mascara = cv2.findHomography(origen_pto, destino_pto, cv2.RANSAC, 5.0)
        matchesMask = mascara.ravel().tolist()

        alto, ancho = imagen1.shape
        puntos = np.float32([[0, 0], [0, alto - 1], [ancho - 1, alto - 1], [ancho - 1, 0]]).reshape(-1, 1, 2)
        destino = cv2.perspectiveTransform(puntos, M)

        imagen2 = cv2.polylines(imagen2, [np.int32(destino)], True, 255, 3, cv2.LINE_AA)
        print("Coincidencias SUF - %d" % (len(aciertos_validos)))

    else:
        print("Coincidencias insuficientes - %d" % (len(aciertos_validos)))
        matchesMask = None

    draw_params = dict(matchColor = (255,0,0),
                       singlePointColor = (0,255,0),
                       matchesMask = matchesMask,
                       flags = 2)

    img3 = cv2.drawMatches(imagenCL1, puntos1, imagenCL2, puntos2, aciertos_validos, None, **draw_params)

    plt.imshow(img3, 'gray'),plt.show()

    return len(aciertos_validos)