import numpy as np
import cv2

def countObject(imagen):
    img = cv2.imread(imagen,0)
    suavizado = cv2.blur(img, (10,10))
    imUmb = cv2.adaptiveThreshold(suavizado, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    inv = cv2.bitwise_not(imUmb)
    kernel = np.ones((10,10), np.uint8)
    cierre = cv2.morphologyEx(inv, cv2.MORPH_CLOSE, kernel)

    cv2.floodFill(cierre, None, (0,0), (0, 255, 255))

    (_, contornos, _) = cv2.findContours(cierre,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dibuja borde
    contornoOk=0
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 100:
            contornoOk=contornoOk+1
            cv2.drawContours(img, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

    print("He encontrado {} objetos".format(len(contornos)))
    cv2.imshow("umbral", imUmb)
    cv2.imshow("inv", inv)
    cv2.imshow("apertuura", cierre)
    cv2.imshow("imagen", img)
    cv2.waitKey(0)



    return contornoOk