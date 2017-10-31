import cv2

camara = cv2.VideoCapture(0)
ret,imagen = camara.read()

while(True):
    cv2.imshow('img1',imagen)
    if cv2.waitKey(1) & 0xFF == ord('y'):
        cv2.imwrite('images/c1.png',imagen)
        cv2.destroyAllWindows()
        break

camara.release()
