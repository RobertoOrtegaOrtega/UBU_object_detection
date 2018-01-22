#autor:Roberto Ortega Ortega

"""aleatorioNuevo:
muestra todos los montajes que hay de cada tipo, ya aprendidos"""

import sqlite3
import tkinter

from src.mostrarImagen import mostrarImagen


def showDB():
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

    listaDatos=list()
    listaDatos1 = list()
    cursor = conexion.execute("SELECT DISTINCT MONTAJE FROM IMAGEN_SEQ;")
    for pos in cursor:
        cursor1 = conexion.execute("SELECT MAX(ID) MONTAJE FROM IMAGEN_SEQ WHERE MONTAJE=?;",(str(pos[0]),))
        for pos1 in cursor1:
            cursor2 = conexion.execute("SELECT NOMBRE MONTAJE FROM IMAGEN_SEQ WHERE ID=?;", (int(pos1[0]),))
            for pos2 in cursor2:
                texto =str(pos2[0])
                listaDatos.append(texto)
    cursor = conexion.execute("SELECT DISTINCT NOMBRE FROM IMAGEN_ALE;")
    for pos in cursor:
        texto = str(pos[0])
        listaDatos1.append(texto)

    showDBGui = tkinter.Tk()
    showDBGui.geometry("1500x800")
    showDBGui.configure(background='LightBlue')

    label1 = tkinter.Label(showDBGui, text="Pulse el que desee borrar", font=("Helvetica", 26),
                           bg='LightBlue', anchor="w", justify="left")
    label1.place(relx=0.5, rely=0.075, anchor="center")

    label2 = tkinter.Label(showDBGui, text="Tabla Secuencial", font=("Helvetica", 26),
                           bg='LightBlue', anchor="w", justify="left")
    label2.place(relx=0.33, rely=0.2, anchor="center")

    label3 = tkinter.Label(showDBGui, text="Tabla Aleatoria", font=("Helvetica", 26),
                           bg='LightBlue', anchor="w", justify="left")
    label3.place(relx=0.66, rely=0.2, anchor="center")

    cnv = tkinter.Canvas(showDBGui,bg='LightBlue')
    cnv.place(relx=0.33, rely=0.6, width=100, height=500,anchor="center")
    cnv1 = tkinter.Canvas(showDBGui, bg='LightBlue')
    cnv1.place(relx=0.66, rely=0.6, width=100, height=500,anchor="center")

    Scroll = tkinter.Scrollbar(showDBGui, orient="vertical", command=cnv.yview)
    Scroll.pack(side="left", fill="y")

    Scroll1 = tkinter.Scrollbar(showDBGui, orient="vertical", command=cnv1.yview)
    Scroll1.pack(side="right", fill="y")

    cnv.configure(yscrollcommand=Scroll.set)
    cnv1.configure(yscrollcommand=Scroll1.set)

    frm = tkinter.Frame(cnv)
    frm1 = tkinter.Frame(cnv1)

    cnv.create_window(0, 0, window=frm, anchor='nw')
    cnv1.create_window(0, 0, window=frm1, anchor='nw')

    for s in listaDatos:
        button = tkinter.Button(frm,text=s,command=lambda s=s: [showDBGui.destroy(),  mostrarImagen(s, 1)])
        button.pack()

    for s in listaDatos1:
        button = tkinter.Button(frm1, text=s,command=lambda s=s: [showDBGui.destroy(), mostrarImagen(s, 0)])
        button.pack()

    frm.update_idletasks()
    frm1.update_idletasks()

    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
    cnv1.configure(scrollregion=(0, 0, frm1.winfo_width(), frm1.winfo_height()))

    showDBGui.mainloop()
