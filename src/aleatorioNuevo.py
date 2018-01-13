#autor:Roberto Ortega Ortega

"""aleatorioNuevo:
Dado un nombre de una pieza, obtendrá una foto tomada con la cámara,
la cual tendrá el nombre dado anteriormente. Además la mostrará en una
interfaz y preguntara si es válida"""

import tkinter

from src.finalizarMontaje import finalizarMontaje
from src.takePhoto import takePhoto


def aleatorioNuevo(nombre):

    #toma de la foto
    takePhoto(nombre + '.png')

    # creacion de interfaz gráfica
    aleatorioNuevoGUI= tkinter.Tk()
    aleatorioNuevoGUI.geometry("1500x800")
    aleatorioNuevoGUI.configure(background='LightBlue')

    label1 = tkinter.Label(aleatorioNuevoGUI, text="¿Es la foto válida?", font=("Helvetica", 16),
                           bg='LightBlue', anchor="w", justify="left")
    label1.place(relx=0.5, rely=0.075, anchor="center")
    foto = tkinter.PhotoImage(file='BaseDatos/' + nombre + '.png')
    label2 = tkinter.Label(image=foto)
    label2.image = foto
    label2.place(relx=0.5, rely=0.5, anchor="center")
    button = tkinter.Button(aleatorioNuevoGUI, text="SI", command=lambda: [aleatorioNuevoGUI.destroy(), finalizarMontaje(nombre,str(nombre[len(nombre)-1:])
                                                                                                                         ,1)])
    button.place(relx=0.33, rely=0.85, anchor="center")
    button1 = tkinter.Button(aleatorioNuevoGUI, text="NO", command=lambda: [aleatorioNuevoGUI.destroy(),aleatorioNuevo(nombre)])
    button1.place(relx=0.66, rely=0.85, anchor="center")
    aleatorioNuevoGUI.mainloop()