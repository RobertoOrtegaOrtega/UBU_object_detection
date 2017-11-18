
#Script principal
from src.compareObjects2 import compareObjects
from src.countObjects import countObject
from src.objectDetection import objectDetection

print('Bienvenido')
print('¿La pieza que desea supervisar tiene una fase de montaje predefinido?')
print('1.- Si, tiene unas fases establecidas las cuales son inmutables')
print('2.- No, la pieze puede ser montada como se desea, siempre que el resultado este bien')
opcion=0
while opcion<1 or opcion>2:
    opcion = int(input('Introduce la opcion deseada'))
previo='l'
while previo != 'n' and previo != 'y':
    print('¿Se conoce con anterioridad las fases de montaje de la pieza o el resultado final?')
    previo = input('(y/n)')

if opcion==1:
    if previo=='y':
        print('catalogo de piezas que pueden ser montadas')
        val = 0
        for i in range(4):
            cad = 'fase' + str(i + 1) + '.png'
            print(cad)
            val = val + compareObjects(cad, 'fase4.png')
        print(val)

    else:
        print('montaje de prueba')
        for i in range(4):
            cad = 'fase' + str(i + 1) + '.png'

            objectDetection(cad)
            objetos = countObject('objetos.png', cad)
else:
    if previo == 'y':
        print('catalogo de piezas que pueden ser montadas')
        #comprobacion estandar de piezas
        """val=0
        for i in range(12):
            print(i)
            cad='sector'+str(i+1)+'.png'
            val=val+compareObjects(cad,cad)
        print(val)"""
        #ejemplo puzzle
        val = 0
        for i in range(12):
            print(i)
            cad = 'sector' + str(i + 1) + '.png'
            val = val + compareObjects(cad, 'puzzle.png')
        print(val)
    else:
        print('montaje de prueba')
        imagen='faseFinal_3.png'
        objectDetection(imagen)
        objetos=countObject('objetos.png',imagen)
