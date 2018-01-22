#autor:Roberto Ortega Ortega

"""aleatorioConocido:
Dado un nombre de una pieza, obtendra a que montaje pertence y
mostrará en una ventana como es el montaje final de esa pieza y
al lado de esta como es la pieza que se esta montando en este momento"""

import sqlite3
import tkinter

from src.takePhoto import takePhoto
from src.validarResultados import validarResultados


def aleatorioConocido(nombre):

    #apertura de la base de datos
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

    #extracion del montaje de la pieza introducida
    aux = conexion.execute("SELECT MONTAJE FROM IMAGEN_ALE WHERE NOMBRE=?;", (nombre[10:len(nombre)-4],))
    for i in aux:
        montaje = str(i[0])
    takePhoto('aux0.png')
    conexion.close()

    #interfaz gráfica
    aleatorioConocidoGui = tkinter.Tk()
    aleatorioConocidoGui.geometry("1500x800")
    aleatorioConocidoGui.title("Montaje Aleatorio")
    aleatorioConocidoGui.configure(background='LightBlue')
    label1 = tkinter.Label(aleatorioConocidoGui, text="¿Es la foto tomada válida?\n", font=("Helvetica", 26),
                           bg='LightBlue')
    label1.place(relx=0.5, rely=0.1, anchor="center")
    label2 = tkinter.Label(aleatorioConocidoGui, text="Imagen cámara\n", font=("Helvetica", 26),
                           bg='LightBlue')
    label2.place(relx=0.3, rely=0.2, anchor="center")
    label3 = tkinter.Label(aleatorioConocidoGui, text="Imagen ideal\n", font=("Helvetica", 26),
                           bg='LightBlue')
    label3.place(relx=0.7, rely=0.2, anchor="center")

    foto1 = tkinter.PhotoImage(file="BaseDatos/aux0.png")
    label4 = tkinter.Label(image=foto1)
    label4.image = foto1
    label4.place(relx=0.3, rely=0.5, anchor="center")
    foto2 = tkinter.PhotoImage(file=nombre)
    label5 = tkinter.Label(image=foto2)
    label5.image = foto2
    label5.place(relx=0.7, rely=0.5, anchor="center")

    boton1 = tkinter.Button(aleatorioConocidoGui, text="Si", bg='white', font=("Helvetica", 16), relief="ridge",
                            command=lambda: [aleatorioConocidoGui.destroy(),validarResultados(montaje,0,0)])
    boton1.place(relx=0.4, rely=0.9,width=200, height=70, anchor="center")
    boton2 = tkinter.Button(aleatorioConocidoGui, text="No", bg='white', font=("Helvetica", 16), relief="ridge",
                            command=lambda: [aleatorioConocidoGui.destroy(),aleatorioConocido(nombre)])
    boton2.place(relx=0.6, rely=0.9,width=200, height=70, anchor="center")

    aleatorioConocidoGui.mainloop()
