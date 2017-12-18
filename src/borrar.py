import sqlite3
import os
def borrar(nombre,opcion):
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
        montaje='Montaje'+str(nombre[len(nombre)-1:])
        cursor =conexion.execute("SELECT NOMBRE from IMAGEN_ALE where montaje=?;", (montaje,))
        for pos in cursor:
            print("-> "+str(pos[0]))
            conexion.execute("DELETE from IMAGEN_ALE where NOMBRE=?;", (str(pos[0]),))
            conexion.commit()
            os.remove('BaseDatos/'+str(pos[0])+'.png')
        cursor =conexion.execute("SELECT NOMBRE from OBJETO where montaje=?;", (montaje,))
        for pos in cursor:
            print("-> " + str(pos[0]))
            conexion.execute("DELETE from OBJETO where NOMBRE=?;", (str(pos[0]),))
            conexion.commit()
            os.remove('BaseDatos/' + str(pos[0]) + '.png')
        conexion.close()
    else:
        cursor =conexion.execute("SELECT * from IMAGEN_SEQ where montaje=?;", (nombre,))
        for pos in cursor:
            print("-> " + str(pos[0]))
        cursor =conexion.execute("SELECT * from DIFERENCIAS where montaje=?;", (nombre,))
        for pos in cursor:
            print("-> " + str(pos[0]))
        conexion.close()