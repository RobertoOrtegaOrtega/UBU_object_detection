import cv2
def takePhoto(nombre):
    camara = cv2.VideoCapture(0)
    ret,imagen = camara.read()
    cv2.imwrite('BaseDatos/'+nombre,imagen)
    camara.release()
