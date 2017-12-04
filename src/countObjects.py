
import cv2
import sqlite3

def countObject(imagen1,imagen2,montaje,tabla):
    conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
    img1 = cv2.imread('BaseDatos/'+imagen1+'.png', 0)
    img1 = cv2.bitwise_not(img1)
    img2 = cv2.imread('BaseDatos/'+imagen2+'.png')
    (_, contornos, _) = cv2.findContours(img1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dibuja borde
    contornoOk=0
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 500:
            contornoOk=contornoOk+1
            print(contornoOk)
            print(area)
            (x, y, w, h) = cv2.boundingRect(c)
            val = conexion.execute('''SELECT max(ID) FROM {};'''.format(tabla))
            for i in val:
                if i[0] == None:
                    val = 1
                else:
                    val = i[0] + 1
            if tabla=='OBJETO':
                conexion.execute('''INSERT INTO OBJETO
                          VALUES (?,?,?)''', (val , 'objeto' + str(contornoOk) + montaje, montaje));
                conexion.commit()
                nombre = 'objeto' + str(contornoOk) + montaje
                cv2.imshow(nombre, img2[y:y + h, x:x + w])
                nombre=nombre+'.png'
                cv2.imwrite('BaseDatos/'+nombre, img2[y:y + h, x:x + w])
                cv2.waitKey(0)
            else:
                nombre = imagen1 + '_' + str(contornoOk)
                conexion.execute('''INSERT INTO DIFERENCIAS
                          VALUES (?,?,?)''', (val , nombre, montaje));
                conexion.commit()
                cv2.imshow(nombre, img2[y:y + h, x:x + w])
                nombre = nombre + '.png'
                cv2.imwrite('BaseDatos/' + nombre, img2[y:y + h, x:x + w])
                cv2.waitKey(0)
    #conexion.close()
    print("He encontrado %d objetos" %contornoOk)
    return contornoOk