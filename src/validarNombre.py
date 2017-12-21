from src.aleatorioConocido import aleatorioConocido
from src.aleatorioNuevo import aleatorioNuevo
from src.secuencialConocido import secuencialConocido
from src.secuencialNuevo import secuencialNuevo


def validarNombre(selectorGui,nombre,opcion,conocido):
    selectorGui.destroy()
    if conocido==1:
        if opcion == 0:
            secuencialNuevo(nombre,1)
        else:
            aleatorioNuevo(nombre)
    else :
        if opcion==0:
            secuencialConocido(nombre,1)
        else:
            print(nombre)
            aleatorioConocido(nombre)