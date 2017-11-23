
import cv2

def countObject(imagen1,imagen2):
    img1 = cv2.imread(imagen1, 0)
    img1 = cv2.bitwise_not(img1)
    img2 = cv2.imread(imagen2)
    (_, contornos, _) = cv2.findContours(img1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # dibuja borde
    contornoOk=0
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 1000:
            print('-----------------')
            contornoOk=contornoOk+1
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 1, cv2.LINE_AA)
            cv2.drawContours(img2, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
            nombre='objeto'+ str(contornoOk-1) + '.png'
            cv2.imshow(nombre, img2[y:y + h, x:x + w])
            cv2.imwrite(nombre, img2[y:y+h,x:x+w])
            cv2.waitKey(0)
    cv2.imshow(nombre, img2)
    cv2.waitKey(0)
    print("He encontrado %d objetos" %contornoOk)
    return contornoOk