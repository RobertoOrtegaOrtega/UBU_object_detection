import sqlite3
import tkinter

from src.compareObjects import compareObjects
from src.compareObjects2 import compareObjects2
from src.countObjects import countObject
from src.objectDetection import objectDetection


def validarResultados(montaje,opcion,contFase):
    if opcion==0:
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
        ok = True
        objectDetection('aux0', montaje, 'NONE1')
        objetos = countObject('auxObjetos', 'aux0', montaje, 'NONE1')
        conexion = sqlite3.connect(ruta)
        cursor = conexion.execute("SELECT NOMBRE FROM OBJETO WHERE MONTAJE=?;", (montaje,))
        cont = 0
        err = False
        for i in cursor:
            if cont != 0:
                maxAciertos = 0
                miobjMax=i[0] + '.png'
                for j in range(objetos):
                    print(i[0] + '.png')
                    miobj = 'auxObjeto_' + str(j + 1)
                    print(miobj)
                    aciertos = compareObjects2(miobj, i[0])
                    print(aciertos)
                    if aciertos > maxAciertos:
                        maxAciertos = aciertos
                        miobjMax = miobj

                validarResultadosGui = tkinter.Tk()
                validarResultadosGui.geometry("1500x800")
                validarResultadosGui.title("Montaje Aleatorio")
                validarResultadosGui.configure(background='LightBlue')
                label1 = tkinter.Label(validarResultadosGui, text="¿Es la foto tomada valida?\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label1.place(relx=0.5, rely=0.1, anchor="center")
                if maxAciertos<8:
                    labelError = tkinter.Label(validarResultadosGui, text="Alerta: Porcentaje de aciertos demasiado bajo\n", font=("Helvetica", 16),
                                           bg='LightBlue',fg="red")
                    labelError.place(relx=0.5, rely=0.15, anchor="center")
                label2 = tkinter.Label(validarResultadosGui, text="Imagen camara\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label2.place(relx=0.3, rely=0.2, anchor="center")
                label3 = tkinter.Label(validarResultadosGui, text="Imagen ideal\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label3.place(relx=0.7, rely=0.2, anchor="center")
                rutaFoto1='BaseDatos/' + miobjMax + '.png'
                foto1 = tkinter.PhotoImage(file="BaseDatos/aux0.png")
                label4 = tkinter.Label(image=foto1)
                label4.image = foto1
                label4.place(relx=0.3, rely=0.5, anchor="center")
                rutaFoto = 'BaseDatos/' + str(i[0]) + '.png'
                foto2 = tkinter.PhotoImage(file=rutaFoto)
                label5 = tkinter.Label(image=foto2)
                label5.image = foto2
                label5.place(relx=0.7, rely=0.5, anchor="center")

                boton1 = tkinter.Button(validarResultadosGui, text="Si", bg='white', font=("Helvetica", 16), relief="ridge",
                                        command=lambda: [validarResultadosGui.destroy()])
                boton1.place(relx=0.5, rely=0.85, anchor="center")
                boton2 = tkinter.Button(validarResultadosGui, text="No", bg='white', font=("Helvetica", 16), relief="ridge",
                                        command=lambda: [validarResultadosGui.destroy()])
                boton2.place(relx=0.6, rely=0.85, anchor="center")

                validarResultadosGui.mainloop()
            if err == False:
                cont = cont + 1
            else:
                print('Montaje erroneo')
                break;

        conexion.close()
    """else:
        salida = 'auxdif'
        compareObjects('aux1', 'aux2', salida)
        objectDetection(salida, montaje, 'NONE')
        if 1 == countObject(salida, 'aux1', montaje, 'NONE'):
            print('Analizo diferencias')
            busqueda = 'dif' + str(contFase - 1) + '_' + str(contFase) + montaje + '_%'
            cursor = conexion.execute("SELECT NOMBRE FROM DIFERENCIAS WHERE NOMBRE LIKE ?;", (busqueda,))
            for pos in cursor:
                texto = 'nombre = ' + str(pos[0])
                print('comparo ' + texto)
                aciertos = compareObjects2('auxdif', str(pos[0]))
                if aciertos < 15:
                    validar = input('¿Es pese a todo la imagen valida? (s/n)')
                    if validar == 'n':
                        err = True
    if err == False:
        img = cv2.imread('BaseDatos/aux1.png')
        cv2.imwrite('BaseDatos/aux2.png', img)
        contFase = contFase + 1
    else:
        print('Montaje erroneo')
        break;"""

