import cv2
def takePhoto(nombre):
    camara = cv2.VideoCapture(0)
    ret,imagen = camara.read()

    while(True):
        cv2.imshow('imagen',imagen)
        if cv2.waitKey(0) & 0xFF == ord('n'):
            cv2.imwrite('BaseDatos/'+nombre,imagen)
            cv2.destroyAllWindows()
            break
    camara.release()
