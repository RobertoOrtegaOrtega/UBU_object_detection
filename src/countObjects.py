
import cv2
import sqlite3
import tkinter
contornoOk=0
def countObject(imagen1,imagen2,montaje,tabla):
    global  contornoOk
    contornoOk=0
    img1 = cv2.imread('BaseDatos/'+imagen1+'.png', 0)
    img1 = cv2.bitwise_not(img1)
    img2 = cv2.imread('BaseDatos/'+imagen2+'.png')
    (_, contornos, _) = cv2.findContours(img1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dibuja borde

    aux=0
    ruta = '../../UBU_object_detection/sqlite/Montajes'
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 500:
            (x, y, w, h) = cv2.boundingRect(c)
            if tabla=='OBJETO':
                ok=True
                while ok:
                    try:
                        conexion = sqlite3.connect(ruta)
                        ok = False
                    except sqlite3.Error:
                        ok = True
                        print("Oops! Base de datos inexsitente, compruebe la ruta e introduzca una nueva")
                        print('Ruta: ' + ruta)
                        ruta = input('Introduce ruta')
                val = conexion.execute('''SELECT max(ID) FROM {};'''.format(tabla))
                for i in val:
                    if i[0] == None:
                        val = 1
                    else:
                        val = i[0] + 1
                contornoOk = contornoOk + 1
                cv2.imshow('Prueba', img2[y:y + h, x:x + w])
                if cv2.waitKey(0) & 0xFF == ord('s'):
                    conexion.execute('''INSERT INTO OBJETO
                              VALUES (?,?,?)''', (val , 'objeto' + str(contornoOk) + montaje, montaje));
                    conexion.commit()
                    nombre = 'objeto' + str(contornoOk) + montaje
                    cv2.imshow(nombre, img2[y:y + h, x:x + w])
                    nombre=nombre+'.png'
                    cv2.imwrite('BaseDatos/'+nombre, img2[y:y + h, x:x + w])
            elif tabla == 'DIFERENCIAS':
                conexion = sqlite3.connect(r'C:\Users\Roberto\PycharmProjects\UBU_object_detection\sqlite\Montajes')
                val = conexion.execute('''SELECT max(ID) FROM {};'''.format(tabla))
                for i in val:
                    if i[0] == None:
                        val = 1
                    else:
                        val = i[0] + 1
                cv2.imshow('Prueba', img2[y:y + h, x:x + w])
                if cv2.waitKey(0) & 0xFF == ord('s'):
                    contornoOk = contornoOk + 1
                    nombre = imagen1 + '_' + str(contornoOk)
                    conexion.execute('''INSERT INTO DIFERENCIAS
                              VALUES (?,?,?)''', (val , nombre, montaje));
                    conexion.commit()
                    nombre = nombre + '.png'
                    cv2.imwrite('BaseDatos/' + nombre, img2[y:y + h, x:x + w])
                cv2.destroyWindow('Prueba')
            elif tabla=='NONE':
                nombre = imagen1 + '_' + str(contornoOk)
                print(nombre)
                cv2.imwrite('BaseDatos/'+nombre+'.png', img2[y:y + h, x:x + w])
                rutaFoto2 = 'BaseDatos/dif' + str(int(imagen2[len(imagen2)-1])-1)+'_'+str(int(imagen2[len(imagen2)-1]))+montaje+'_1.png'
                countGui = tkinter.Tk()
                countGui.geometry("1500x800")
                countGui.title("Montaje Aleatorio")
                countGui.configure(background='LightBlue')
                label1 = tkinter.Label(countGui, text="¿Es la diferencia encontrada valida?\n",
                                       font=("Helvetica", 16),
                                       bg='LightBlue')
                label1.place(relx=0.5, rely=0.1, anchor="center")
                label2 = tkinter.Label(countGui, text="Diferencia\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label2.place(relx=0.3, rely=0.2, anchor="center")
                label3 = tkinter.Label(countGui, text="Imagen ideal\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label3.place(relx=0.7, rely=0.2, anchor="center")
                rutaFoto = 'BaseDatos/'+nombre+'.png'
                foto1 = tkinter.PhotoImage(file=rutaFoto)
                label4 = tkinter.Label(image=foto1)
                label4.image = foto1
                label4.place(relx=0.3, rely=0.5, anchor="center")

                foto2 = tkinter.PhotoImage(file=rutaFoto2)
                label4 = tkinter.Label(image=foto2)
                label4.image = foto2
                label4.place(relx=0.7, rely=0.5, anchor="center")

                boton1 = tkinter.Button(countGui, text="Si", bg='white', font=("Helvetica", 16),
                                        relief="ridge",
                                        command=lambda: [countGui.destroy(),incrementaObj()])
                boton1.place(relx=0.5, rely=0.85, anchor="center")
                boton2 = tkinter.Button(countGui, text="No", bg='white', font=("Helvetica", 16),
                                        relief="ridge",
                                        command=lambda: [countGui.destroy()])
                boton2.place(relx=0.6, rely=0.85, anchor="center")
                countGui.mainloop()
            else:
                nombre = 'auxObjeto_' + str(contornoOk)
                cv2.imwrite('BaseDatos/' + nombre + '.png', img2[y:y + h, x:x + w])
                rutaFoto2 = 'BaseDatos/aux0.png'
                countGui = tkinter.Tk()
                countGui.geometry("1500x800")
                countGui.title("Montaje Aleatorio")
                countGui.configure(background='LightBlue')
                label1 = tkinter.Label(countGui, text="¿Es la diferencia encontrada valida?\n",
                                       font=("Helvetica", 16),
                                       bg='LightBlue')
                label1.place(relx=0.5, rely=0.1, anchor="center")
                label2 = tkinter.Label(countGui, text="Diferencia\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label2.place(relx=0.3, rely=0.2, anchor="center")
                label3 = tkinter.Label(countGui, text="Imagen ideal\n", font=("Helvetica", 16),
                                       bg='LightBlue')
                label3.place(relx=0.7, rely=0.2, anchor="center")
                rutaFoto = 'BaseDatos/' + nombre + '.png'
                foto1 = tkinter.PhotoImage(file=rutaFoto)
                label4 = tkinter.Label(image=foto1)
                label4.image = foto1
                label4.place(relx=0.3, rely=0.5, anchor="center")

                foto2 = tkinter.PhotoImage(file=rutaFoto2)
                label4 = tkinter.Label(image=foto2)
                label4.image = foto2
                label4.place(relx=0.7, rely=0.5, anchor="center")

                boton1 = tkinter.Button(countGui, text="Si", bg='white', font=("Helvetica", 16),
                                        relief="ridge",
                                        command=lambda: [countGui.destroy(), incrementaObj()])
                boton1.place(relx=0.5, rely=0.85, anchor="center")
                boton2 = tkinter.Button(countGui, text="No", bg='white', font=("Helvetica", 16),
                                        relief="ridge",
                                        command=lambda: [countGui.destroy()])
                boton2.place(relx=0.6, rely=0.85, anchor="center")
                countGui.mainloop()
    #conexion.close()
    print("He encontrado %d objetos" %contornoOk)
    return contornoOk

def incrementaObj():
    global contornoOk
    contornoOk=contornoOk+1