#Script principal
print('Bienvenido')
print('¿La pieza que desea supervisar tiene una fase de montaje predefinido?')
print('1.- Si, tiene unas fases establecidas las cuales son inmutables')
print('2.- No, la pieze puede ser montada como se desea, siempre que el resultado este bien')
opcion=0
while opcion<1 or opcion>2:
    opcion = input('Introduce la opcion deseada')
previo='n'
while previo == 'n' or previo == 'y':
    print('¿Se conoce con anterioridad las fases de montaje de la pieza o el resultado final?')
    previo = input('(y/n)',)
if opcion==1:
    if previo=='y':
        print('catalogo de piezas que pueden ser montadas')
    else:
        print('montaje de prueba')
else:
    if previo == 'y':
        print('catalogo de piezas que pueden ser montadas')
    else:
        print('montaje de prueba')

