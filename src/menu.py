
#Script principal
import sqlite3
import cv2
from src.compareObjects2 import compareObjects
from src.countObjects import countObject
from src.objectDetection import objectDetection

conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
conexion.execute('''DELETE FROM IMAGEN_ALE WHERE ID=2;''');
conexion.commit()
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

print('Bienvenido')
print('¿La pieza que desea supervisar tiene una fase de montaje predefinido?')
print('1.- Si, tiene unas fases establecidas las cuales son inmutables')
print('2.- No, la pieze puede ser montada como se desea, siempre que el resultado este bien')
opcion=0
while opcion<1 or opcion>2:
    opcion = int(input('Introduce la opcion deseada'))

if opcion==1:
    previo = 'l'
    while previo != 'n' and previo != 'y':
        print('¿Es la pieza una de las siguientes?')
        cursor = conexion.execute("SELECT nombre,tipo,montaje from IMAGEN")
        for pos in cursor:
            print("Nombre = ", pos[0])
            print("Tipo = ", pos[1])
            print("Montaje = ", pos[2], "\n")
        previo = input('(y/n)')
    if previo=='y':
        print('catalogo de piezas que pueden ser montadas')
        val = 0
        for i in range(4):
            cad = 'fase' + str(i + 1) + '.png'
            print(cad)
            val = val + compareObjects(cad, 'fase4.png')
        print(val)

    else:
        previo = 'l'
        while previo != 'n' and previo != 'y':
            print('¿Se conoce con anterioridad las fases de montaje de la pieza o el resultado final?')
            previo = input('(y/n)')
        print('montaje de prueba')
        for i in range(4):
            cad = 'fase' + str(i + 1) + '.png'

            objectDetection(cad)
            objetos = countObject('objetos.png', cad)
    conexion.close()
else:
    conexion.commit();
    previo = 'n'
    print('¿Es la pieza una de las siguientes?')
    cursor = conexion.execute("SELECT nombre,montaje from IMAGEN_ALE")
    for pos in cursor:
        print("¿Es esta pieza la que desea? ")
        cad=str(pos[0])+'.png'
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
    if previo == 'n':
        print('montaje de prueba')
        print("Falta sacar la foto")
        id=2
        nombre='FaseFinal_2'
        montaje='Montaje2'
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        conexion.execute('''INSERT INTO IMAGEN_ALE
                  VALUES (?,?,?)''', (id, nombre, montaje));
        conexion.commit()
        conexion.close()
        objectDetection(nombre,montaje)
        objetos=countObject('objetos'+montaje,nombre+'.png',montaje)
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;",(montaje,))
        cont=0
        for i in cursor:
            print(i[0])
            if cont != 0:
                aciertos = compareObjects(nombre+'.png', i[0] + '.png')
                if aciertos>15:
                    print("Pieza encontrada")
                else:
                    print("Pieza NO encontrada")
            cont = cont + 1
        conexion.close()
    else:
        conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;",(montaje,))
        cont=0
        for i in cursor:
            if cont != 0:
                print(i[0])
                aciertos=compareObjects(cad, i[0]+'.png')
                if aciertos>15:
                    print("Pieza encontrada")
                else:
                    print("Pieza NO encontrada")
            cont=cont+1
        conexion.close()