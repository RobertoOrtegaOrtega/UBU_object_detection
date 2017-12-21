import tkinter

from src.selector import selector
from src.showDB import showDB
from os import listdir
import os

while True:
    ruta='BaseDatos'
    for cosa in listdir(ruta):
        if cosa[:3]=='aux':
            os.remove('BaseDatos/'+cosa)
    gui = tkinter.Tk()
    gui.geometry("1500x800")
    gui.title("Menu")
    gui.configure(background='LightBlue')
    botonBD = tkinter.Button(gui, text="BASE DE DATOS",fg='blue',bg='white',font=("Helvetica", 16), relief="ridge", command=lambda:[gui.destroy(),showDB()])
    botonBD .place(relx=0.9, rely=0.1, anchor="center")
    label1 = tkinter.Label(gui, text="¿Que tipo de montaje se va a supervisar?\n",font=("Helvetica", 16),bg='LightBlue')
    label1.place(relx=0.5, rely=0.4, anchor="center")
    boton1 = tkinter.Button(gui, text="Secuencial",bg='white',font=("Helvetica", 16), relief="ridge", command=lambda:[gui.destroy(),selector(0)])
    boton1.place(relx=0.4, rely=0.6, anchor="center")
    boton2 = tkinter.Button(gui, text="Aleatorio",bg='white',font=("Helvetica", 16), relief="ridge", command=lambda:[gui.destroy(),selector(1)])
    boton2.place(relx=0.6, rely=0.6, anchor="center")
    label2 = tkinter.Label(gui, text="Monitorizacion de montajes industriales\n"
                                    "Realizada por Roberto Ortega Ortega\n"
                                    "Tutorizada por Pedro Snachez\n"
                                    "La aplicacion es capaz de controlar y aprender montajes industriales gracias al tratamiento de imagenes.\n",font=("Helvetica", 12),bg='LightBlue',anchor="w", justify="left")
    label2.place(relx=0.0, rely=0.9)
    gui.mainloop()