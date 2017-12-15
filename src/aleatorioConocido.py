from src.compareObjects2 import compareObjects2
from src.countObjects import countObject
from src.objectDetection import objectDetection
from src.takePhoto import takePhoto
import cv2
import sqlite3
import tkinter

def aleatorioConocido(nombre):
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
    ok = True
    print(nombre[:len(nombre)-4])
    aux = conexion.execute("SELECT MONTAJE FROM IMAGEN_ALE WHERE NOMBRE=?;", (nombre[:len(nombre)-4],))
    for i in aux:
        montaje = str(i[0])
        print("Mi montaje "+montaje)
    takePhoto('aux0.png')
    aleatorioConocidoGui = tkinter.Tk()
    aleatorioConocidoGui.geometry("1500x800")
    aleatorioConocidoGui.title("Montaje Aleatorio")
    aleatorioConocidoGui.configure(background='LightBlue')
    label1 = tkinter.Label(aleatorioConocidoGui, text="¿Es la foto tomada valida?\n", font=("Helvetica", 16),
                           bg='LightBlue')
    label1.place(relx=0.5, rely=0.1, anchor="center")
    label2 = tkinter.Label(aleatorioConocidoGui, text="Imagen camara\n", font=("Helvetica", 16),
                           bg='LightBlue')
    label2.place(relx=0.3, rely=0.2, anchor="center")
    label3 = tkinter.Label(aleatorioConocidoGui, text="Imagen ideal\n", font=("Helvetica", 16),
                           bg='LightBlue')
    label3.place(relx=0.7, rely=0.2, anchor="center")

    foto1 = tkinter.PhotoImage(file="BaseDatos/aux0.png")
    label4 = tkinter.Label(image=foto1)
    label4.image = foto1
    label4.place(relx=0.3, rely=0.5, anchor="center")
    rutaFoto='BaseDatos/'+nombre
    foto2 = tkinter.PhotoImage(file=rutaFoto)
    label5 = tkinter.Label(image=foto2)
    label5.image = foto2
    label5.place(relx=0.7, rely=0.5, anchor="center")

    boton1 = tkinter.Button(aleatorioConocidoGui, text="Si", bg='white', font=("Helvetica", 16), relief="ridge",
                            command=lambda: [aleatorioConocidoGui.destroy(),validarResultados])
    boton1.place(relx=0.4, rely=0.85, anchor="center")
    boton2 = tkinter.Button(aleatorioConocidoGui, text="No", bg='white', font=("Helvetica", 16), relief="ridge",
                            command=lambda: [aleatorioConocidoGui.destroy(),aleatorioConocido(nombre)])
    boton2.place(relx=0.6, rely=0.85, anchor="center")

    aleatorioConocidoGui.mainloop()
    objectDetection('aux0', montaje, 'NONE1')
    objetos = countObject('auxObjetos', 'aux0', montaje, 'NONE1')
    conexion = sqlite3.connect(ruta)
    cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;", (montaje,))
    cont = 0
    err = False
    for i in cursor:
        if cont != 0:
            maxAciertos = 0
            for j in range(objetos):
                print(i[0] + '.png')
                miobj = 'auxObjeto_' + str(j + 1)
                print(miobj)
                aciertos = compareObjects2(miobj, i[0])
                print(aciertos)
                if aciertos > maxAciertos:
                    maxAciertos = aciertos
                    miobjMax = miobj

            print(maxAciertos)
            print(miobjMax)
            print(i[0])
            img1 = cv2.imread('BaseDatos/' + miobjMax + '.png')
            img2 = cv2.imread('BaseDatos/' + i[0] + '.png')
            cv2.imshow('objeto1', img1)
            cv2.imshow('objeto2', img2)
            cv2.waitKey(0)
            if maxAciertos < 8:
                validar = input('¿Es pese a todo la imagen valida? (s/n)')
                if validar == 'n':
                    err = True
        if err == False:
            cont = cont + 1
        else:
            print('Montaje erroneo')
            break;

    conexion.close()