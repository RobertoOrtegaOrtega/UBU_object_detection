#autor:Roberto Ortega Ortega

"""finalizarMontaje:
algotimo qie se encarga de finalizar el aprendizaje de nuevos montajes,
ya sean aleatorios o secuenciales"""

import sqlite3

from src.compareObjects import compareObjects
from src.compareObjects2 import compareObjects2
from src.countObjects import countObject
from src.objectDetection import objectDetection


def finalizarMontaje(nombre,montaje,opcion):

    #abro base de datos
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

    #opcion de montajes secuenciales
    if opcion==0:
        salida = 'dif' + str(montaje - 1) + '_' + str(montaje) + 'Montaje' + str(nombre[len(nombre)-1])
        compareObjects('Fase_' + str(montaje - 1) + 'Montaje' + str(nombre[len(nombre)-1]), nombre, salida)
        objectDetection(salida, 'Montaje' + str(nombre[len(nombre)-1]), 'DIFERENCIAS')
        num = 0
        while num != 1:
            num = countObject(salida, nombre, 'Montaje' + str(nombre[len(nombre)-1]), 'DIFERENCIAS')
        busqueda = salida + '_%'
        cursor = conexion.execute("SELECT NOMBRE FROM DIFERENCIAS WHERE NOMBRE LIKE ?;", (busqueda,))
        for pos in cursor:
            texto = 'nombre = ' + str(pos[0])
            compareObjects2(nombre, str(pos[0]))

    # opcion de montajes aleatorios
    else:
        montaje = 'Montaje' + str(nombre[len(nombre) - 1:])
        tabla='OBJETO'
        conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (nombre[len(nombre)-1:], nombre, montaje))
        conexion.commit()
        objectDetection(nombre, montaje, tabla)
        countObject('objetos'+montaje, nombre, montaje, tabla)
        conexion = sqlite3.connect(ruta)
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;", (montaje,))
        cont = 0
        for i in cursor:
            print(i[0] + '.png')
            if cont != 0:
                aciertos = compareObjects2(nombre, i[0])
                if aciertos > 15:
                    print("Pieza encontrada")
                else:
                    print("Pieza NO encontrada")
            cont = cont + 1
        conexion.close()