import sqlite3
import tkinter

def showDB():

    datos = tkinter.Tk()
    datos.geometry("1500x800")
    datos.title("Base de datos")
    datos.configure(background='LightBlue')
    scrollbar = tkinter.Scrollbar(datos)
    scrollbar.pack(side="right", fill="y")

    listaDatos = tkinter.Listbox(datos, yscrollcommand=scrollbar.set,width=100)
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
    cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM OBJETO;")
    listaDatos.insert("end", "--> TABLA OBJETO")
    listaDatos.insert("end", "\t\t\tID\t\t\t|\t\t\tNOMBRE\t\t\t|\t\t\tMONTAJE")
    for pos in cursor:
        texto =str(pos[0]) +str(pos[1]) +str(pos[2])
        listaDatos.insert("end", texto)
    cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM IMAGEN_ALE;")
    listaDatos.insert("end", "\n")
    listaDatos.insert("end", "--> TABLA IMAGEN ALEATORIA")
    listaDatos.insert("end", "\t\t\tID\t\t\t|\t\t\tNOMBRE\t\t\t|\t\t\tMONTAJE")
    for pos in cursor:
        texto =str(pos[0]) +str(pos[1]) +str(pos[2])
        listaDatos.insert("end", texto)
    cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM IMAGEN_SEQ;")
    listaDatos.insert("end", "--> TABLA IMAGEN SECUENCIAL")
    for pos in cursor:
        texto =str(pos[0])+ str(pos[1]) +str(pos[2])
        listaDatos.insert("end", texto)
    cursor = conexion.execute("SELECT ID,NOMBRE,MONTAJE FROM DIFERENCIAS;")
    listaDatos.insert("end", "\n")
    listaDatos.insert("end", "--> TABLA DIFERENCIAS")
    listaDatos.insert("end", "\t\t\tID\t\t\t|\t\t\tNOMBRE\t\t\t|\t\t\tMONTAJE")
    for pos in cursor:
        texto =str(pos[0])+ str(pos[1]) +str(pos[2])
        listaDatos.insert("end", texto)

    listaDatos.pack(padx=30, pady=30, ipadx=300, ipady=400)

    scrollbar.config(command=listaDatos.yview)
    datos.mainloop()
