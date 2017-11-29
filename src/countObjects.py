
import cv2
import sqlite3

def countObject(imagen1,imagen2,montaje):
    conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
    img1 = cv2.imread(imagen1+'.png', 0)
    img1 = cv2.bitwise_not(img1)
    img2 = cv2.imread(imagen2)
    (_, contornos, _) = cv2.findContours(img1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dibuja borde
    contornoOk=0
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 1000:
            print('-----------------')
            contornoOk=contornoOk+1
            (x, y, w, h) = cv2.boundingRect(c)
            conexion.execute('''DELETE FROM OBJETO WHERE ID=?;''',(str(contornoOk+11),));
            conexion.execute('''INSERT INTO OBJETO
                      VALUES (?,?,?)''', (str(contornoOk+11) , 'objeto' + str(contornoOk) + montaje, montaje));
            conexion.commit()
            nombre = 'objeto' + str(contornoOk) + montaje
            cv2.imshow(nombre, img2[y-30:y + h+30, x-30:x + w+30])
            nombre=nombre+'.png'
            cv2.imwrite(nombre, img2[y-30:y + h+30, x-30:x + w+30])
            cv2.waitKey(0)
    conexion.close()
    print("He encontrado %d objetos" %contornoOk)
    return contornoOk