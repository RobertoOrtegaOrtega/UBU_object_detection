import cv2
import numpy as np
import sqlite3

def objectDetection(imagen,montaje,tabla):
    mi_imagen='BaseDatos/'+imagen+'.png'
    img = cv2.imread(mi_imagen, 0)
    suavizado = cv2.blur(img, (10, 10))
    imUmb = cv2.adaptiveThreshold(suavizado, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((10, 10), np.uint8)
    imUmb = cv2.morphologyEx(imUmb, cv2.MORPH_OPEN, kernel)
    inv = cv2.bitwise_not(imUmb)
    kernel = np.ones((3,3), np.uint8)
    inv = cv2.morphologyEx(inv, cv2.MORPH_OPEN, kernel)
    mascara = cv2.bitwise_not(inv)
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
        aux = cv2.bitwise_and(aux, aux, dst=None, mask=mascara)
        if count > 400:
            break
        bordes = aux
        count = count + 1

    aux=aux*255
    conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
    # conexion.execute('''DELETE FROM OBJETO WHERE ID=10;''');
    val = conexion.execute('''SELECT max(ID) FROM {};'''.format(tabla))
    for i in val:
        if i[0] == None:
            val = 1
        else:
            val = i[0] + 1
    if tabla=='OBJETO':
        conexion.execute('''INSERT INTO OBJETO
              VALUES (?,?,?)''',(str(val),"objetos"+montaje,montaje));
        conexion.commit()
        conexion.close()
        nombre='BaseDatos/objetos'+montaje+'.png'
        cv2.imwrite(nombre, aux)
    else:
        conexion.execute('''INSERT INTO DIFERENCIAS
                      VALUES (?,?,?)''', (str(val), imagen, montaje));
        conexion.commit()
        conexion.close()
        cv2.imwrite(mi_imagen, aux)