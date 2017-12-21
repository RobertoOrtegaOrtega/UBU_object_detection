import sqlite3

from src.compareObjects import compareObjects
from src.compareObjects2 import compareObjects2
from src.countObjects import countObject
from src.objectDetection import objectDetection


def finalizarMontaje(nombre,montaje,opcion):
    ok = True
    ruta = '../../UBU_object_detection/sqlite/Montajes'
    while ok:
        try:
            conexion = sqlite3.connect(ruta)
            ok = False
        except sqlite3.Error:
            ok = True
            print("Oops! Base de datos inexsitente, compruebe la ruta e introduzca una nueva")
            print('Ruta: ' + ruta)
            ruta = input('Introduce ruta')
    if opcion==0:
        print("Secuencial")
        print("Mi nombre: "+nombre)
        print("Num fase: "+str(montaje))
        print("Mi montaje: Montaje" + str(nombre[len(nombre)-1]))
        salida = 'dif' + str(montaje - 1) + '_' + str(montaje) + 'Montaje' + str(nombre[len(nombre)-1])
        print("salida1: "+salida)
        compareObjects('Fase_' + str(montaje - 1) + 'Montaje' + str(nombre[len(nombre)-1]), nombre, salida)
        objectDetection(salida, 'Montaje' + str(nombre[len(nombre)-1]), 'DIFERENCIAS')
        num = 0
        while num != 1:
            num = countObject(salida, nombre, 'Montaje' + str(nombre[len(nombre)-1]), 'DIFERENCIAS')
        busqueda = salida + '_%'
        cursor = conexion.execute("SELECT NOMBRE FROM DIFERENCIAS WHERE NOMBRE LIKE ?;", (busqueda,))
        for pos in cursor:
            texto = 'nombre = ' + str(pos[0])
            print(texto)
            compareObjects2(nombre, str(pos[0]))
    else:
        print("Aleatoria")
        montaje = 'Montaje' + str(nombre[len(nombre) - 1:])
        tabla='OBJETO'
        conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (nombre[len(nombre)-1:], nombre, montaje))
        conexion.commit()
        objectDetection(nombre, montaje, tabla)
        objetos = countObject('objetos' + montaje, nombre, montaje, tabla)
        print(objetos)
        conexion = sqlite3.connect(ruta)
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;", (montaje,))
        cont = 0
        print("yeeeeeeee2")
        for i in cursor:
            print(i[0] + '.png')
            if cont != 0:
                print(i[0] + '.png')
                aciertos = compareObjects2(nombre, i[0])
                if aciertos > 15:
                    print("Pieza encontrada")
                else:
                    print("Pieza NO encontrada")
            cont = cont + 1
        conexion.close()
    print("extaer objetos")