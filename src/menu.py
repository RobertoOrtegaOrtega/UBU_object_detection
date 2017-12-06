
#Script principal
import sqlite3
import cv2

from src.compareObjects import compareObjects
from src.compareObjects2 import compareObjects2
from src.countObjects import countObject
from src.objectDetection import objectDetection
from src.takePhoto import takePhoto

conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
conexion.execute('''DELETE FROM IMAGEN_SEQ WHERE MONTAJE=?;''',('Montaje6',));
conexion.commit()
conexion.execute('''DELETE FROM DIFERENCIAS WHERE MONTAJE=?;''',('Montaje6',));
conexion.commit()
val=conexion.execute('''SELECT max(ID) FROM IMAGEN_ALE;''')
for i in val:
    print(i[0])
cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM OBJETO;")
print("TABLA OBJETO")
for pos in cursor:
    texto = 'ID = ' + str(pos[0]) + ' // Nombre = ' + str(pos[1]) + ' // Montaje = ' + str(pos[2])
    print(texto)
cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM IMAGEN_ALE;")
print("TABLA IMAGEN ALEATORIA")
for pos in cursor:
    texto = 'ID = ' + str(pos[0]) + ' // Nombre = ' + str(pos[1]) + ' // Montaje = ' + str(pos[2])
    print(texto)
cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM IMAGEN_SEQ;")
print("TABLA IMAGEN SECUENCIAL")
for pos in cursor:
    texto = 'ID = ' + str(pos[0]) + ' // Nombre = ' + str(pos[1]) + ' // Montaje = ' + str(pos[2])
    print(texto)
cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM DIFERENCIAS;")
print("TABLA DIFERENCIAS")
for pos in cursor:
    texto = 'ID = ' + str(pos[0]) + ' // Nombre = ' + str(pos[1]) + ' // Montaje = ' + str(pos[2])
    print(texto)

print('Bienvenido')
print('¿La pieza que desea supervisar tiene una fase de montaje predefinido?')
print('1.- Si, tiene unas fases establecidas las cuales son inmutables')
print('2.- No, la pieze puede ser montada como se desea, siempre que el resultado este bien')
opcion=0
while opcion<1 or opcion>2:
    opcion = int(input('Introduce la opcion deseada'))

if opcion==1:
    tabla='DIFERENCIAS'
    previo = 'n'
    print('¿Es la pieza una de las siguientes?')
    cursor = conexion.execute("SELECT DISTINCT MONTAJE FROM IMAGEN_SEQ")
    for pos in cursor:
        if pos != None:
            print(pos[0])
            maxID = conexion.execute("SELECT max(ID) FROM IMAGEN_SEQ WHERE MONTAJE LIKE ?;",(pos[0],))
            for i in maxID:
                valID = i[0]
            print(valID)
            cursor2 = conexion.execute("SELECT NOMBRE FROM IMAGEN_SEQ  WHERE ID=?;", (valID,))
            for pos2 in cursor2:
                print("¿Es esta pieza la que desea? ")
                print(pos2[0])
                cad = 'BaseDatos/' + str(pos2[0]) + '.png'
                nombre = str(pos[0])
                montaje = str(pos[0])
                texto = 'Nombre = ' + str(pos2[0]) + ' // Montaje = ' + str(pos[0])
                img = cv2.imread(cad)
                cv2.imshow(texto, img)
                if cv2.waitKey(0) & 0xFF == ord('y'):
                    cv2.destroyAllWindows()
                    previo = 'y'
                    break;
                cv2.destroyAllWindows()
        else:
            print('Base de datos vacia')
    if previo == 'n':
        print('montaje de prueba')
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        val = conexion.execute('''SELECT max(ID) FROM IMAGEN_SEQ;''')
        for i in val:
            if i[0] == None:
                montaje='Montaje1'
                val = 1
            else:
                montaje='Montaje'+str(montaje[len(montaje)-1])
                val = i[0] + 1
        contFase=1
        flag=True
        while flag:
            nombre = 'Fase_' + str(contFase)+montaje
            takePhoto(nombre + '.png')
            conexion.execute('''INSERT INTO IMAGEN_SEQ
                      VALUES (?,?,?)''', (val+contFase-1, nombre, montaje));
            conexion.commit()
            if contFase!=1:
                salida='dif'+str(contFase-1)+'_'+str(contFase)+montaje
                compareObjects('Fase_' + str(contFase-1)+montaje,nombre,salida)
                objectDetection(salida, montaje,tabla)
                if 1 ==countObject(salida, nombre, montaje,tabla):
                    busqueda=salida+'_%'
                    cursor = conexion.execute("SELECT NOMBRE FROM DIFERENCIAS WHERE NOMBRE LIKE ?;",(busqueda,))
                    for pos in cursor:
                        texto = 'nombre = ' + str(pos[0])
                        print(texto)
                        aciertos = compareObjects2(nombre, str(pos[0]))
                        if aciertos <15:
                            break;
                else:
                    print('Error')
            if 'y'==input('¿Tiene el montaje más fases? (y/n)'):
                contFase=contFase+1
            else:
                flag=False
    else:
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM IMAGEN_SEQ WHERE MONTAJE=?;", (montaje,))
        contFase=1
        for pos in cursor:
            texto = 'ID = ' + str(pos[0]) + ' // Nombre = ' + str(pos[1]) + ' // Montaje = ' + str(pos[2])
            print(texto)
            takePhoto('aux1.png')
            if contFase != 1:
                salida = 'auxdif'
                compareObjects('aux1', 'aux2', salida)
                objectDetection(salida, montaje, 'NONE')
                if 1 == countObject(salida, 'aux1', montaje, 'NONE'):
                    busqueda = salida + '_%'
                    cursor = conexion.execute("SELECT NOMBRE FROM DIFERENCIAS WHERE NOMBRE LIKE ?;", (busqueda,))
                    for pos in cursor:
                        texto = 'nombre = ' + str(pos[0])
                        print(texto)
                        aciertos = compareObjects2('auxdif', str(pos[0]))
                        if aciertos < 15:
                            break;
            img=cv2.imread('BaseDatos/aux1.png')
            cv2.imwrite('BaseDatos/aux2.png',img)
            contFase=contFase+1
        conexion.close()
else:
    tabla = 'OBJETO'
    previo = 'n'
    print('¿Es la pieza una de las siguientes?')
    cursor = conexion.execute("SELECT nombre,montaje from IMAGEN_ALE")
    for pos in cursor:
        if pos != None:
            print("¿Es esta pieza la que desea? ")
            cad='BaseDatos/'+str(pos[0])+'.png'
            nombre=str(pos[0])
            montaje=str(pos[1])
            texto='Nombre = ' +str(pos[0])+' // Montaje = '+str(pos[1])
            img=cv2.imread(cad)
            cv2.imshow(texto,img)
            if cv2.waitKey(0) & 0xFF == ord('y'):
                cv2.destroyAllWindows()
                previo = 'y'
                break;
            cv2.destroyAllWindows()
        else:
            print('Base de datos vacia')
    if previo == 'n':
        print('montaje de prueba')
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        val = conexion.execute('''SELECT max(ID) FROM IMAGEN_ALE;''')
        for i in val:
            if i[0] == None:
                val=1
            else:
                val=i[0]+1
        nombre='FaseFinal_'+str(val)
        montaje='Montaje'+str(val)
        takePhoto(nombre+'.png')
        conexion.execute('''INSERT INTO IMAGEN_ALE
                  VALUES (?,?,?)''', (val, nombre, montaje));
        conexion.commit()
        conexion.close()
        objectDetection(nombre,montaje,tabla)
        objetos=countObject('objetos'+montaje,nombre,montaje,tabla)
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;",(montaje,))
        cont=0
        for i in cursor:
            if cont != 0:
                print(i[0]+'.png')
                aciertos=compareObjects2(nombre, i[0])
                if aciertos>15:
                    print("Pieza encontrada")
                else:
                    print("Pieza NO encontrada")
            cont=cont+1
        conexion.close()
    else:
        takePhoto('aux0.png')
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;",(montaje,))
        cont=0
        for i in cursor:
            if cont != 0:
                print(i[0]+'.png')
                aciertos=compareObjects2('aux0', i[0])
                if aciertos>15:
                    print("Pieza encontrada")
                else:
                    print("Pieza NO encontrada")
            cont=cont+1
        conexion.close()