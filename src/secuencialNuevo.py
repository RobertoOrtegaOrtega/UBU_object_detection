#autor:Roberto Ortega Ortega

"""secuencialNuevo:
Dado un nombre de una pieza, obtendrá una foto tomada con la cámara,
la cual tendrá el nombre dado anteriormente. Además la mostrará en una
interfaz y preguntara si es válida"""

import sqlite3
import tkinter
import os

from src.finalizarMontaje import finalizarMontaje
from src.takePhoto import takePhoto


def secuencialNuevo(montaje,fase):

    #toma de foto
    nombre='Fase_'+str(fase)+'Montaje'+str(montaje)
    takePhoto(nombre + '.png')

    #creacion ventana grafica
    secuencialNuevoGUI = tkinter.Tk()
    secuencialNuevoGUI.geometry("1500x800")
    secuencialNuevoGUI.configure(background='LightBlue')

    label1 = tkinter.Label(secuencialNuevoGUI, text="¿Es la foto válida?", font=("Helvetica", 26),
                           bg='LightBlue', anchor="w", justify="left")
    label1.place(relx=0.5, rely=0.075, anchor="center")
    foto = tkinter.PhotoImage(file='BaseDatos/' + nombre + '.png')
    label2 = tkinter.Label(image=foto)
    label2.image = foto
    label2.place(relx=0.5, rely=0.5, anchor="center")
    if fase != 1:
        button = tkinter.Button(secuencialNuevoGUI, text="SI", bg='white', font=("Helvetica", 16), relief="ridge",
                                command=lambda: [secuencialNuevoGUI.destroy(),insertar(nombre,montaje), finalizarMontaje(nombre, fase,0),secuencialNuevo(montaje, fase+1)])
        button.place(relx=0.33, rely=0.85, anchor="center")
        button1 = tkinter.Button(secuencialNuevoGUI, text="NO", bg='white', font=("Helvetica", 16), relief="ridge",
                                 command=lambda: [secuencialNuevoGUI.destroy(), secuencialNuevo(montaje,fase)])
        button1.place(relx=0.66, rely=0.85, anchor="center")
        button2 = tkinter.Button(secuencialNuevoGUI, text="FINALIZAR", bg='white', font=("Helvetica", 16), relief="ridge",
                                 command=lambda: [secuencialNuevoGUI.destroy(),eliminaObj('BaseDatos/' + nombre + '.png')])
        button2.place(relx=0.5, rely=0.95, anchor="center")
    else:
        button = tkinter.Button(secuencialNuevoGUI, text="SI", bg='white', font=("Helvetica", 16), relief="ridge",
                                command=lambda: [secuencialNuevoGUI.destroy(),insertar(nombre,montaje), secuencialNuevo(montaje, fase+1)])
        button.place(relx=0.33, rely=0.9, anchor="center")
        button1 = tkinter.Button(secuencialNuevoGUI, text="NO", bg='white', font=("Helvetica", 16), relief="ridge",
                                 command=lambda: [secuencialNuevoGUI.destroy(), secuencialNuevo(montaje, fase)])
        button1.place(relx=0.66, rely=0.9, anchor="center")
    secuencialNuevoGUI.mainloop()

"""metodo que hace inserciones de nuevas fases en la base de datos"""
def insertar(nombre,montaje):
    montaje = 'Montaje' + str(montaje)
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
    maxID = conexion.execute("SELECT max(ID) FROM IMAGEN_SEQ;")
    for i in maxID:
        valID = i[0]
    conexion.execute('''INSERT INTO IMAGEN_SEQ VALUES (?,?,?)''', (i[0]+1, nombre, montaje));
    conexion.commit()

"""metodo que elimina imagenes erroneas"""
def eliminaObj(ruta):
    os.remove(ruta)