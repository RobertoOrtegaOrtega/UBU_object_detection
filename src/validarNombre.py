import tkinter

from src.aleatorioConocido import aleatorioConocido
from src.secuencialConocido import secuencialConocido


def validarNombre(selectorGui,cuadroTexto,misNombres,opcion ):
    check = cuadroTexto.get()
    print("Mi check: "+check)

    if check in misNombres:
        selectorGui.destroy()
        if opcion==0:
            secuencialConocido(check,1)
        else:
            aleatorioConocido(check)
    elif len(check)==0:
        if opcion == 0:
            print("Montaje secuencial")
        else:
            print("Montaje aleatorio")
    else:
        error = tkinter.Tk()
        error.title("Error")
        error.configure(background='LightBlue')
        label1 = tkinter.Label(error, text="ERROR: nombre incorrecto", font=("Helvetica", 16),
                               bg='LightBlue', anchor="w", justify="left")
        label1.place(relx=0.5, rely=0.5, anchor="center")
        error.mainloop()
