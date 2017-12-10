
import cv2
import sqlite3

def countObject(imagen1,imagen2,montaje,tabla):

    img1 = cv2.imread('BaseDatos/'+imagen1+'.png', 0)
    img1 = cv2.bitwise_not(img1)
    img2 = cv2.imread('BaseDatos/'+imagen2+'.png')
    (_, contornos, _) = cv2.findContours(img1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dibuja borde
    contornoOk=0
    ruta = '../../UBU_object_detection/sqlite/Montajes'
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 500:
            (x, y, w, h) = cv2.boundingRect(c)
            if tabla=='OBJETO':
                ok=True
                while ok:
                    try:
                        conexion = sqlite3.connect(ruta)
                        ok = False
                    except sqlite3.Error:
                        ok = True
                        print("Oops! Base de datos inexsitente, compruebe la ruta e introduzca una nueva")
                        print('Ruta: ' + ruta)
                        ruta = input('Introduce ruta')
                val = conexion.execute('''SELECT max(ID) FROM {};'''.format(tabla))
                for i in val:
                    if i[0] == None:
                        val = 1
                    else:
                        val = i[0] + 1
                contornoOk = contornoOk + 1
                cv2.imshow('Prueba', img2[y:y + h, x:x + w])
                if cv2.waitKey(0) & 0xFF == ord('s'):
                    conexion.execute('''INSERT INTO OBJETO
                              VALUES (?,?,?)''', (val , 'objeto' + str(contornoOk) + montaje, montaje));
                    conexion.commit()
                    nombre = 'objeto' + str(contornoOk) + montaje
                    cv2.imshow(nombre, img2[y:y + h, x:x + w])
                    nombre=nombre+'.png'
                    cv2.imwrite('BaseDatos/'+nombre, img2[y:y + h, x:x + w])
            elif tabla == 'DIFERENCIAS':
                conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
                val = conexion.execute('''SELECT max(ID) FROM {};'''.format(tabla))
                for i in val:
                    if i[0] == None:
                        val = 1
                    else:
                        val = i[0] + 1
                cv2.imshow('Prueba', img2[y:y + h, x:x + w])
                if cv2.waitKey(0) & 0xFF == ord('s'):
                    contornoOk = contornoOk + 1
                    nombre = imagen1 + '_' + str(contornoOk)
                    conexion.execute('''INSERT INTO DIFERENCIAS
                              VALUES (?,?,?)''', (val , nombre, montaje));
                    conexion.commit()
                    nombre = nombre + '.png'
                    cv2.imwrite('BaseDatos/' + nombre, img2[y:y + h, x:x + w])
                cv2.destroyWindow('Prueba')
            elif tabla=='NONE':
                contornoOk = contornoOk + 1
                nombre = imagen1 + '_' + str(contornoOk)
                cv2.imwrite('BaseDatos/auxdif.png', img2[y:y + h, x:x + w])
            else:
                contornoOk = contornoOk + 1
                nombre = 'auxObjeto_' + str(contornoOk)
                cv2.imwrite('BaseDatos/'+nombre+'.png', img2[y:y + h, x:x + w])
    #conexion.close()
    print("He encontrado %d objetos" %contornoOk)
    return contornoOk