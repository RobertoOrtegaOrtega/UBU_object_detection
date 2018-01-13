# autor:Roberto Ortega Ortega

"""borrar:
algoritmo que eliminara los datos seleccionados, tanto las entradas
en la base de datos, como las imagenes asociadas"""

import sqlite3
import os

def borrar(nombre,opcion):

    #apertura base de datos
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

    #opcion de montajes aleatorios
    if opcion==0:
        montaje='Montaje'+str(nombre[len(nombre)-1:])
        cursor =conexion.execute("SELECT NOMBRE from IMAGEN_ALE where montaje=?;", (montaje,))
        #recorro todas las entradas encontradas en la tabla imagen_ale ara borrarlas
        for pos in cursor:
            print("-> "+str(pos[0]))
            conexion.execute("DELETE from IMAGEN_ALE where NOMBRE=?;", (str(pos[0]),))
            conexion.commit()
            os.remove('BaseDatos/'+str(pos[0])+'.png')
        cursor1 =conexion.execute("SELECT NOMBRE from OBJETO where montaje=?;", (montaje,))
        # recorro todas las entradas encontradas en la tabla objeto ara borrarlas
        for pos1 in cursor1:
            print("-> " + str(pos1[0]))

            conexion.execute("DELETE from OBJETO"
                             " where NOMBRE=?;", (str(pos1[0]),))
            conexion.commit()
            os.remove('BaseDatos/' + str(pos1[0]) + '.png')
        conexion.close()

    #opcion de montajes secuenciales
    else:
        montaje = 'Montaje' + str(nombre[len(nombre) - 1:])
        cursor =conexion.execute("SELECT NOMBRE from IMAGEN_SEQ where montaje=?;", (montaje,))
        # recorro todas las entradas encontradas en la tabla imagen_seq ara borrarlas
        for pos in cursor:
            print("-> "+str(pos[0]))
            conexion.execute("DELETE from IMAGEN_SEQ where NOMBRE=?;", (str(pos[0]),))
            conexion.commit()
            os.remove('BaseDatos/'+str(pos[0])+'.png')
        cursor1 =conexion.execute("SELECT NOMBRE from DIFERENCIAS where montaje=?;", (montaje,))
        # recorro todas las entradas encontradas en la tabla diferencias ara borrarlas
        for pos1 in cursor1:
            print("-> " + str(pos1[0]))
            conexion.execute("DELETE from DIFERENCIAS"
                             " where NOMBRE=?;", (str(pos1[0]),))
            conexion.commit()
            os.remove('BaseDatos/' + str(pos1[0]) + '.png')
        conexion.close()