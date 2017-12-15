import cv2
import numpy as np
def compareObjects(imagen1,imagen2,salida):
    imagen1 = cv2.imread('BaseDatos/'+imagen1+'.png')
    imagen2 = cv2.imread('BaseDatos/'+imagen2+'.png')

    diferencias = cv2.absdiff(imagen1, imagen2)

    imagen_gris = cv2.cvtColor(diferencias, cv2.COLOR_BGR2GRAY)

    """cv2.imshow('Imagen1', imagen1)
    cv2.imshow('Imagen2', imagen2)
    cv2.imshow('Diferencias detectadas', diferencias)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
    cv2.imwrite('BaseDatos/'+salida+'.png', diferencias)