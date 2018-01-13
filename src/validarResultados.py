import sqlite3
import tkinter
import cv2

from src.compareObjects import compareObjects
from src.compareObjects2 import compareObjects2
from src.countObjects import countObject
from src.objectDetection import objectDetection


def validarResultados(montaje,opcion,contFase):
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
    if opcion==0:
        objectDetection('aux0', montaje, 'NONE1')
        num=conexion.execute("SELECT count(NOMBRE) FROM OBJETO WHERE MONTAJE=?;", (montaje,))
        for n in num:
            num=n[0]-1
        print(num)
        while num != countObject('auxObjetos', 'aux0', montaje, 'NONE1'):
            print("Error")
        conexion = sqlite3.connect(ruta)
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;", (montaje,))

        cont = 0
        for i in cursor:
            if cont != 0:
                maxAciertos = 0
                miobjMax=i[0] + '.png'
                for j in range(num):
                    print(i[0] + '.png')
                    miobj = 'auxObjeto_' + str(j + 1)
                    print(miobj)
                    aciertos = compareObjects2(miobj, i[0])
                    print(aciertos)
                    if aciertos > maxAciertos:
                        maxAciertos = aciertos
                        miobjMax = miobj
                print("Max: "+str(maxAciertos) +"->"+miobjMax+"//"+i[0] + '.png')
                validarResultadosGui = tkinter.Tk()
                validarResultadosGui.geometry("1500x800")
                validarResultadosGui.title("Montaje Aleatorio")
                validarResultadosGui.configure(background='LightBlue')
                label1 = tkinter.Label(validarResultadosGui, text="¿Es el objeto valido?\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label1.place(relx=0.5, rely=0.1, anchor="center")
                if maxAciertos<8:
                    labelError = tkinter.Label(validarResultadosGui, text="Alerta: Porcentaje de aciertos demasiado bajo\n", font=("Helvetica", 16),
                                           bg='LightBlue',fg="red")
                    labelError.place(relx=0.5, rely=0.15, anchor="center")
                label2 = tkinter.Label(validarResultadosGui, text="Objeto encontrado\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label2.place(relx=0.3, rely=0.2, anchor="center")
                label3 = tkinter.Label(validarResultadosGui, text="Objeto original\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label3.place(relx=0.7, rely=0.2, anchor="center")
                rutaFoto1='BaseDatos/' + miobjMax + '.png'
                foto1 = tkinter.PhotoImage(file=rutaFoto1)
                label4 = tkinter.Label(image=foto1)
                label4.image = foto1
                label4.place(relx=0.3, rely=0.5, anchor="center")
                rutaFoto = 'BaseDatos/' + str(i[0]) + '.png'
                foto2 = tkinter.PhotoImage(file=rutaFoto)
                label5 = tkinter.Label(image=foto2)
                label5.image = foto2
                label5.place(relx=0.7, rely=0.5, anchor="center")

                boton1 = tkinter.Button(validarResultadosGui, text="Sigiente", bg='white', font=("Helvetica", 16), relief="ridge",
                                        command=lambda: [validarResultadosGui.destroy()])
                boton1.place(relx=0.5, rely=0.85, anchor="center")


                validarResultadosGui.mainloop()
            cont=cont+1
        conexion.close()



    else:
        print("contador Fase: "+str(contFase))
        salida = 'auxdif'+str(contFase-2)
        foto1='auxFase'+str(contFase-1)
        foto2 = 'auxFase' + str(contFase)
        compareObjects(foto1, foto2, salida)
        objectDetection(salida, montaje, 'NONE')
        while 1!=countObject(salida, foto2, montaje, 'NONE'):
            print("error")
        busqueda = 'dif' + str(contFase - 1) + '_' + str(contFase) + montaje + '_1'
        aciertos = compareObjects2(salida+'_0', busqueda)
        foto1 = salida+'_0'
        foto2 = busqueda
        validarResultadosGui = tkinter.Tk()
        validarResultadosGui.geometry("1500x800")
        validarResultadosGui.title("Montaje Seciencial")
        validarResultadosGui.configure(background='LightBlue')
        label1 = tkinter.Label(validarResultadosGui, text="¿Es la diferencia encontrada correcta?\n", font=("Helvetica", 16),
                               bg='LightBlue')
        label1.place(relx=0.5, rely=0.1, anchor="center")
        if aciertos < 8:
            labelError = tkinter.Label(validarResultadosGui, text="Alerta: Porcentaje de aciertos demasiado bajo\n",
                                       font=("Helvetica", 16),
                                       bg='LightBlue', fg="red")
            labelError.place(relx=0.5, rely=0.15, anchor="center")
        label2 = tkinter.Label(validarResultadosGui, text="Imagen camara\n", font=("Helvetica", 16),
                               bg='LightBlue')
        label2.place(relx=0.3, rely=0.2, anchor="center")
        label3 = tkinter.Label(validarResultadosGui, text="Imagen ideal\n", font=("Helvetica", 16),
                               bg='LightBlue')
        label3.place(relx=0.7, rely=0.2, anchor="center")
        rutaFoto1 = 'BaseDatos/auxFase'+str(contFase)+'.png'
        foto1 = tkinter.PhotoImage(file=rutaFoto1)
        label4 = tkinter.Label(image=foto1)
        label4.image = foto1
        label4.place(relx=0.3, rely=0.5, anchor="center")
        rutaFoto = 'BaseDatos/Fase_' + str(contFase)+montaje + '.png'
        foto2 = tkinter.PhotoImage(file=rutaFoto)
        label5 = tkinter.Label(image=foto2)
        label5.image = foto2
        label5.place(relx=0.7, rely=0.5, anchor="center")

        boton1 = tkinter.Button(validarResultadosGui, text="Siguiente", bg='white', font=("Helvetica", 16), relief="ridge",
                                command=lambda: [validarResultadosGui.destroy()])
        boton1.place(relx=0.5, rely=0.85, anchor="center")

        validarResultadosGui.mainloop()

