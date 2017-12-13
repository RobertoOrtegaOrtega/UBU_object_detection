import cv2


def selector(opcion):
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
    elif opcion == 2:
        tabla = 'OBJETO'
        previo = 'n'
        print('¿Es la pieza una de las siguientes?')
        cursor = conexion.execute("SELECT nombre,montaje from IMAGEN_ALE")
        for pos in cursor:
            if pos != None:
                print("¿Es esta pieza la que desea? ")
                cad = 'BaseDatos/' + str(pos[0]) + '.png'
                nombre = str(pos[0])
                montaje = str(pos[1])
                texto = 'Nombre = ' + str(pos[0]) + ' // Montaje = ' + str(pos[1])
                img = cv2.imread(cad)
                cv2.imshow(texto, img)
                if cv2.waitKey(0) & 0xFF == ord('y'):
                    cv2.destroyAllWindows()
                    previo = 'y'
                    break;
                cv2.destroyAllWindows()
            else:
                print('Base de datos vacia')