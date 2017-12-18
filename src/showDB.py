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
    """conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (1, 'FaseFinal_1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (2, 'FaseFinal_2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (3, 'FaseFinal_3', 'Montaje3'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_ALE VALUES (?,?,?)''', (4, 'FaseFinal_4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (1, 'objetosMontaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (2, 'objeto1Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (3, 'objeto2Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (4, 'objeto3Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (5, 'objeto4Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (6, 'objeto5Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (7, 'objeto6Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (8, 'objeto7Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (9, 'objeto8Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (10, 'objeto9Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (11, 'objetosMontaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (12, 'objeto1Montaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (13, 'objeto2Montaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (14, 'objeto3Montaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (15, 'objeto4Montaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (16, 'objeto5Montaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (17, 'objeto6Montaje2', 'Montaje2'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (18, 'objetosMontaje3', 'Montaje3'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (19, 'objeto1Montaje3', 'Montaje3'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (20, 'objeto2Montaje3', 'Montaje3'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (21, 'objeto3Montaje3', 'Montaje3'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (22, 'objeto4Montaje3', 'Montaje3'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (23, 'objetosMontaje4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (24, 'objeto1Montaje4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (25, 'objeto2Montaje4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (26, 'objeto3Montaje4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (27, 'objeto4Montaje4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO OBJETO VALUES (?,?,?)''', (28, 'objeto5Montaje4', 'Montaje4'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_SEQ VALUES (?,?,?)''', (1, 'Fase_1Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_SEQ VALUES (?,?,?)''', (2, 'Fase_2Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_SEQ VALUES (?,?,?)''', (3, 'Fase_3Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_SEQ VALUES (?,?,?)''', (4, 'Fase_4Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO IMAGEN_SEQ VALUES (?,?,?)''', (5, 'Fase_5Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (1, 'dif1_2Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (2, 'dif1_2Montaje1_1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (3, 'dif2_3Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (4, 'dif2_3Montaje1_1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (5, 'dif3_4Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (6, 'dif3_4Montaje1_1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (7, 'dif4_5Montaje1', 'Montaje1'));
    conexion.commit()
    conexion.execute('''INSERT INTO DIFERENCIAS VALUES (?,?,?)''', (8, 'dif4_5Montaje1_1', 'Montaje1'));
    conexion.commit()"""
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
    print(listaDatos)
    print(listaDatos1)

    showDBGui = tkinter.Tk()
    showDBGui.geometry("1500x800")
    showDBGui.configure(background='LightBlue')

    label1 = tkinter.Label(showDBGui, text="Pulse el que desee borrar", font=("Helvetica", 16),
                           bg='LightBlue', anchor="w", justify="left")
    label1.place(relx=0.5, rely=0.075, anchor="center")

    label2 = tkinter.Label(showDBGui, text="Tabla Aleatoria", font=("Helvetica", 16),
                           bg='LightBlue', anchor="w", justify="left")
    label2.place(relx=0.33, rely=0.2, anchor="center")

    label3 = tkinter.Label(showDBGui, text="Tabla Aleatoria", font=("Helvetica", 16),
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
        print(s)
        button = tkinter.Button(frm,text=s,command=lambda: [showDBGui.destroy(),  mostrarImagen(s, 1)])
        button.pack()

    for s in listaDatos1:
        print(s)
        button = tkinter.Button(frm1, text=s,command=lambda: [showDBGui.destroy(), mostrarImagen(s, 0)])
        button.pack()

    frm.update_idletasks()
    frm1.update_idletasks()

    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
    cnv1.configure(scrollregion=(0, 0, frm1.winfo_width(), frm1.winfo_height()))

    showDBGui.mainloop()
