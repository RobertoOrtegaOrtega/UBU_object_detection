import cv2
import sqlite3
import tkinter
from PIL import Image, ImageTk

from src.validarNombre import validarNombre


def selector(opcion):
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

    misImagenes = list()
    if opcion==0:
        tabla='DIFERENCIAS'
        previo = 'n'
        cursor = conexion.execute("SELECT DISTINCT MONTAJE FROM IMAGEN_SEQ")
        for pos in cursor:
            if pos != None:
                print(pos[0])
                maxID = conexion.execute("SELECT max(ID) FROM IMAGEN_SEQ WHERE MONTAJE LIKE ?;",(pos[0],))
                for i in maxID:
                    valID = i[0]
                print(valID)
                cursor2 = conexion.execute("SELECT NOMBRE FROM IMAGEN_SEQ  WHERE ID=?;", (valID,))
                for pos2 in cursor2:
                    cad = 'BaseDatos/' + str(pos2[0]) + '.png'
                    misImagenes.append(cad)
    elif opcion == 1:
        tabla = 'OBJETO'
        previo = 'n'
        print('¿Es la pieza una de las siguientes?')
        cursor = conexion.execute("SELECT nombre,montaje from IMAGEN_ALE")
        for pos in cursor:
            if pos != None:
                cad = 'BaseDatos/' + str(pos[0]) + '.png'
                misImagenes.append(cad)
        ## Main window
    misNombres = list()

    selectorGui = tkinter.Tk()
    selectorGui.geometry("1500x800")
    selectorGui.title("Selector Secuecial")
    selectorGui.configure(background='LightBlue')
    label1 = tkinter.Label(selectorGui, text="¿Es una de las siguientes la imagen deseada?", font=("Helvetica", 16),
                           bg='LightBlue', anchor="w", justify="left")
    label1.place(relx=0.5, rely=0.075, anchor="center")
    cnv = tkinter.Canvas(selectorGui)
    cnv.place(x=350, y=90, width=800, height=600)

    Scroll = tkinter.Scrollbar(selectorGui, orient="vertical", command=cnv.yview)
    Scroll.pack(side="right", fill="y")
    cnv.configure(yscrollcommand=Scroll.set)

    frm = tkinter.Frame(cnv)
    cnv.create_window(0, 0, window=frm, anchor='nw')

    for s in misImagenes:
        texto = tkinter.StringVar()
        miTexto = tkinter.Label(frm, textvariable=texto)
        miNombre=s[10:]
        misNombres.append(miNombre)
        texto.set(miNombre)
        miTexto.pack()
        im = Image.open(s)
        tkimage = ImageTk.PhotoImage(im)
        myvar = tkinter.Label(frm, image=tkimage)
        myvar.image = tkimage
        myvar.pack()

    frm.update_idletasks()

    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
    cuadroTexto = tkinter.Entry(selectorGui)
    cuadroTexto.place(relx=0.33, rely=0.95, anchor="center")
    boton1 = tkinter.Button(selectorGui, text="Continuar", bg='white', font=("Helvetica", 16), relief="ridge",
                            command=lambda: [validarNombre(selectorGui, cuadroTexto, misNombres, opcion)])
    boton1.place(relx=0.66, rely=0.95, anchor="center")
    selectorGui.mainloop()


