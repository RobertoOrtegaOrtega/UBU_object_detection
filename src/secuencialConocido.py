#autor:Roberto Ortega Ortega

"""secuencialConocido:
Dado un nombre de una pieza, obtendra a que montaje pertence y
mostrará en una ventana como es la fase actual de esa pieza y
al lado de esta como es la pieza que se esta montando en este momento"""

import sqlite3
import tkinter

from src.takePhoto import takePhoto
from src.validarResultados import validarResultados


def secuencialConocido(nombre,fase):

    #apertura base de datos
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

    #obtengo montaje
    aux = conexion.execute("SELECT MONTAJE FROM IMAGEN_SEQ WHERE NOMBRE=?;", (nombre[len('BaseDatos/'):len(nombre) - 4],))
    for i in aux:
        montaje = str(i[0])
    cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM IMAGEN_SEQ WHERE MONTAJE=?;", (montaje,))

    contFase = 1

    #recorro todas las fases

    for pos in cursor:

        if contFase==fase:
            takePhoto('auxFase' + str(contFase) + '.png')
            secuencialConocidoGui = tkinter.Tk()
            secuencialConocidoGui.geometry("1500x800")
            secuencialConocidoGui.title("Montaje Aleatorio")
            secuencialConocidoGui.configure(background='LightBlue')
            label1 = tkinter.Label(secuencialConocidoGui, text="¿Es la foto tomada valida?\n", font=("Helvetica", 26),
                                   bg='LightBlue')
            label1.place(relx=0.5, rely=0.1, anchor="center")
            label2 = tkinter.Label(secuencialConocidoGui, text="Imagen cámara\n", font=("Helvetica", 26),
                                   bg='LightBlue')
            label2.place(relx=0.3, rely=0.2, anchor="center")
            label3 = tkinter.Label(secuencialConocidoGui, text="Imagen ideal\n", font=("Helvetica", 26),
                                   bg='LightBlue')
            label3.place(relx=0.7, rely=0.2, anchor="center")

            foto1 = tkinter.PhotoImage(file="BaseDatos/auxFase"+str(contFase)+".png")
            label4 = tkinter.Label(image=foto1)
            label4.image = foto1
            label4.place(relx=0.3, rely=0.5, anchor="center")
            rutaFoto = 'BaseDatos/' + str(pos[1])+'.png'
            foto2 = tkinter.PhotoImage(file=rutaFoto)
            label5 = tkinter.Label(image=foto2)
            label5.image = foto2
            label5.place(relx=0.7, rely=0.5, anchor="center")
            if contFase!=1:
                boton1 = tkinter.Button(secuencialConocidoGui, text="Si", bg='white', font=("Helvetica", 16), relief="ridge",
                                        command=lambda: [secuencialConocidoGui.destroy(),validarResultados(montaje, 1, contFase), secuencialConocido(nombre,fase+1)])
                boton1.place(relx=0.4, rely=0.9, anchor="center")
                boton2 = tkinter.Button(secuencialConocidoGui, text="No", bg='white', font=("Helvetica", 16), relief="ridge",
                                        command=lambda: [secuencialConocidoGui.destroy(), secuencialConocido(nombre,fase)])
                boton2.place(relx=0.6, rely=0.9, anchor="center")
            else:
                boton1 = tkinter.Button(secuencialConocidoGui, text="Si", bg='white', font=("Helvetica", 16),
                                        relief="ridge",
                                        command=lambda: [secuencialConocidoGui.destroy(),
                                                         secuencialConocido(nombre, fase + 1)])
                boton1.place(relx=0.4, rely=0.9, anchor="center")
                boton2 = tkinter.Button(secuencialConocidoGui, text="No", bg='white', font=("Helvetica", 16),
                                        relief="ridge",
                                        command=lambda: [secuencialConocidoGui.destroy(),
                                                         secuencialConocido(nombre, fase)])
                boton2.place(relx=0.6, rely=0.9, anchor="center")

            secuencialConocidoGui.mainloop()
        contFase=contFase+1
    conexion.close()
