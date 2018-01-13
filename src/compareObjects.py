# autor:Roberto Ortega Ortega

"""compareObjects:
algoritmo que resta en valor absoluto dos imagenes para asi
obtener las diferencias"""

import cv2

def compareObjects(imagen1,imagen2,salida):

    #obtengo las imagenes
    imagen1 = cv2.imread('BaseDatos/'+imagen1+'.png')
    imagen2 = cv2.imread('BaseDatos/'+imagen2+'.png')

    #resto las imagentes
    diferencias = cv2.absdiff(imagen1, imagen2)

    imagen_gris = cv2.cvtColor(diferencias, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('BaseDatos/'+salida+'.png', diferencias)