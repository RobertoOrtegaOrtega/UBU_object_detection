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
            else:
                print("Base datos vadia")
        print(cad)
    elif opcion == 1:
        print('¿Es la pieza una de las siguientes?')
        cursor = conexion.execute("SELECT nombre,montaje from IMAGEN_ALE")
        for pos in cursor:
            if pos != None:
                cad = 'BaseDatos/' + str(pos[0]) + '.png'
                print(cad)
                misImagenes.append(cad)
            else:
                print("Base datos vadia")
        print(cad)

    selectorGui = tkinter.Tk()
    selectorGui.geometry("1500x800")
    if opcion==0:
        selectorGui.title("Selector Secuecial")
    else:
        selectorGui.title("Selector Aleatorio")
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
        im = Image.open(s)
        tkimage = ImageTk.PhotoImage(im)
        button = tkinter.Button(frm, image=tkimage,command=lambda s=s: [validarNombre(selectorGui, s, opcion,0)])
        button.image = tkimage
        button.pack()

    frm.update_idletasks()

    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
    if opcion==0:
        aux=str(misImagenes[len(misImagenes)-1])
        nuevoNombre=str(int(aux[len(aux)-5])+1)


    else:
        nuevoNombre = 'FaseFinal_'+str(int(misImagenes[len(misImagenes)-1][20:21])+1)
    boton1 = tkinter.Button(selectorGui, text="Nuevo Montaje", bg='white', font=("Helvetica", 16), relief="ridge",
                            command=lambda: [validarNombre(selectorGui, nuevoNombre, opcion,1)])
    boton1.place(relx=0.5, rely=0.95, anchor="center")
    selectorGui.mainloop()


