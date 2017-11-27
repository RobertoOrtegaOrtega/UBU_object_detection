import cv2
import numpy as np
import sqlite3

def objectDetection(imagen,montaje):
    imagen=imagen+'.png'
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
    conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
    conexion.execute('''DELETE FROM OBJETO;''');
    conexion.execute('''INSERT INTO OBJETO
          VALUES (?,?,?)''',(str(1),"objetos"+montaje,montaje));
    conexion.commit()
    conexion.close()
    nombre='objetos'+montaje+'.png'
    cv2.imwrite(nombre, aux)