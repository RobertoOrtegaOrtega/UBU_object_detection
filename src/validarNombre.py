from src.aleatorioConocido import aleatorioConocido
from src.aleatorioNuevo import aleatorioNuevo
from src.secuencialConocido import secuencialConocido


def validarNombre(selectorGui,nombre,opcion,conocido):

    if conocido==1:
        if opcion == 0:
            print("Montaje secuencial")
        else:
            aleatorioNuevo(nombre)
    else :
        selectorGui.destroy()
        if opcion==0:
            secuencialConocido(nombre,1)
        else:
            aleatorioConocido(nombre)