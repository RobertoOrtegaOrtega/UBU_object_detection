import tkinter

from src.borrar import borrar


def mostrarImagen(nombre,opcion):
    mostrarGUI = tkinter.Tk()
    mostrarGUI.geometry("1500x800")
    mostrarGUI.configure(background='LightBlue')

    label1 = tkinter.Label(mostrarGUI, text="¿Es el montaje que desea borrar?", font=("Helvetica", 16),
                           bg='LightBlue', anchor="w", justify="left")
    label1.place(relx=0.5, rely=0.075, anchor="center")
    foto1 = tkinter.PhotoImage(file='BaseDatos/'+nombre+'.png')
    label2 = tkinter.Label(image=foto1)
    label2.image = foto1
    label2.place(relx=0.5, rely=0.5, anchor="center")
    button = tkinter.Button(mostrarGUI, text="SI", command=lambda: [mostrarGUI.destroy(), borrar(nombre, opcion)])
    button.place(relx=0.33, rely=0.85, anchor="center")
    button1 = tkinter.Button(mostrarGUI, text="NO", command=lambda: [mostrarGUI.destroy()])
    button1.place(relx=0.66, rely=0.85, anchor="center")
    mostrarGUI.mainloop()
