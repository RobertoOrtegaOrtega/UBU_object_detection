import cv2
import numpy as np

def objectDetection(imagen):
    img = cv2.imread(imagen, 0)
    suavizado = cv2.blur(img, (10, 10))
    imUmb = cv2.adaptiveThreshold(suavizado, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((10, 10), np.uint8)
    imUmb = cv2.morphologyEx(imUmb, cv2.MORPH_OPEN, kernel)
    inv = cv2.bitwise_not(imUmb)
    dim = np.shape(inv)
    bordes = np.zeros(dim)
    # primera y ultima fila
    bordes[0] = 1;
    bordes[dim[0] - 1] = 1;
    # primera y ultima col
    for i in range(dim[0]):
        bordes[i][0] = 1;
        bordes[i][dim[1] - 1] = 1;
    fin = False;
    kernel = np.ones((5, 5), np.uint8)
    count = 1
    while (~fin):
        aux = cv2.dilate(bordes, kernel, iterations=1)
        aux = cv2.bitwise_and(aux, aux, dst=None, mask=imUmb)
        if count > 400:
            break
        bordes = aux
        count = count + 1

    aux=aux*255
    cv2.imshow("mis objetos", aux)
    cv2.imwrite('objetos.png', aux)
    cv2.imshow("imagen", img)
    cv2.waitKey(0)