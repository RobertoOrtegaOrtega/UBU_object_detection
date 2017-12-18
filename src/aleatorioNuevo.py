import sqlite3
import cv2

from src.takePhoto import takePhoto


def aleatorioNuevo(nombre):
    ruta = '../../UBU_object_detection/sqlite/Montajes'
    ok = True
    while ok:
        try:
            conexion = sqlite3.connect(ruta)
            ok = False
        except sqlite3.Error:
            ok = True
            print("Oops! Base de datos inexsitente, compruebe la ruta e introduzca una nueva")
            print('Ruta: ' + ruta)
            ruta = input('Introduce ruta')
    print('montaje de prueba')
    print(nombre)
    montaje = 'Montaje' + str(nombre[len(nombre)-1:])
    print(montaje)
    takePhoto(nombre + '.png')
    conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (nombre[len(nombre)-1:], nombre, montaje))
    conexion.commit()
    conexion.close()
    """objectDetection(nombre, montaje, tabla)
    objetos = countObject('objetos' + montaje, nombre, montaje, tabla)
    conexion = sqlite3.connect(ruta)
    cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;", (montaje,))
    cont = 0
    for i in cursor:
        if cont != 0:
            print(i[0] + '.png')
            aciertos = compareObjects2(nombre, i[0])
            if aciertos > 15:
                print("Pieza encontrada")
            else:
                print("Pieza NO encontrada")
        cont = cont + 1
    conexion.close()
    # comparar objeto por objeto"""