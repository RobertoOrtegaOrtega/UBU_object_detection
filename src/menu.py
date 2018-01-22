#autor:Roberto Ortega Ortega

"""menu:
algoritmo básico desde el cual se redirige a todos los demas, y que además
eliminalas fotos auxiliares usadas por el programa en otras ejecuciones"""

import tkinter

from src.selector import selector
from src.showDB import showDB
from os import listdir
import os


def info():
    ayuda = tkinter.Tk()
    ayuda.geometry("725x375")
    ayuda.title("Ayuda")
    ayuda.configure(background='LightBlue')
    label = tkinter.Label(ayuda, text="Monitorización de montajes industriales.\n"
                                     "Realizada por Roberto Ortega Ortega.\n"
                                     "Tutorizada por Pedro Luis Sánchez Ortega y Cesar Represa Pérez.\n\n"
                                     "Aplicación que es capaz de aprender y gestionar montajes industriales\n"
                                      "de manera simulada.\n"
                                    "Puede gestinar dos tipos de montajes:\n\n"
                                    "Montajes Secuenciales: en el cual se comparan las diferencias de fase\n"
                                    "a fase. Esta diferencia tiene que ser la misma que la de la fase aprendida\n"
                                    "para que el montaje sea validado\n\n"
                                  "Montajes Aleatorios: en el cual se comparan los obejos de la fase final\n"
                                  "siendo necesario para validar un montaje, que dichos ojetos sean los mismos\n"
                                  "que los del montaje aprendido\n\n"
                                    "Contacto: roo0002@alu.ubu.es\n\n",
                           font=("Helvetica", 12), bg='LightBlue', anchor="w", justify="left")
    label.place(relx=0.1, rely=0.1)
    ayuda.mainloop()


while True:

    #eliminación de las imagenes auxiliares
    ruta='BaseDatos'
    for cosa in listdir(ruta):
        if cosa[:3]=='aux':
            os.remove('BaseDatos/'+cosa)

    #creacion de la interfaz
    gui = tkinter.Tk()
    gui.geometry("1500x800")
    gui.title("Menu")
    gui.configure(background='LightBlue')
    botonAyuda = tkinter.Button(gui, text="Infromación", fg='blue', bg='white', font=("Helvetica", 16), relief="ridge", command=lambda: [info()])
    botonAyuda.place(relx=0.75, rely=0.1, anchor="center")
    botonBD = tkinter.Button(gui, text="BASE DE DATOS",fg='blue',bg='white',font=("Helvetica", 16), relief="ridge", command=lambda:[gui.destroy(),showDB()])
    botonBD .place(relx=0.9, rely=0.1, anchor="center")
    label1 = tkinter.Label(gui, text="¿Que tipo de montaje se va a supervisar?\n",font=("Helvetica", 26),bg='LightBlue')
    label1.place(relx=0.5, rely=0.4, anchor="center")
    boton1 = tkinter.Button(gui, text="Secuencial",bg='white',font=("Helvetica", 16), relief="ridge", command=lambda:[gui.destroy(),selector(0)])
    boton1.place(relx=0.35, rely=0.7,width=200, height=70, anchor="center")
    boton2 = tkinter.Button(gui, text="Aleatorio",bg='white',font=("Helvetica", 16), relief="ridge", command=lambda:[gui.destroy(),selector(1)])
    boton2.place(relx=0.66, rely=0.7,width=200, height=70, anchor="center")
    gui.mainloop()