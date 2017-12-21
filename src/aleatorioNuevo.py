import tkinter

from src.finalizarMontaje import finalizarMontaje
from src.takePhoto import takePhoto


def aleatorioNuevo(nombre):
    print('montaje de prueba')
    print(nombre)
    montaje = 'Montaje' + str(nombre[len(nombre)-1:])
    print(montaje)
    takePhoto(nombre + '.png')

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