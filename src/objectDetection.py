import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread('imagen.png')

plt.subplot(221), plt.imshow(imagen), plt.title('Original')
plt.xticks([]), plt.yticks([])

imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

mediana = cv2.blur(imagenGris, (20,20))
#No funciona con mala luz, o extraña
#t, imUmb = cv2.threshold(imagenGris, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

imUmb = cv2.adaptiveThreshold (mediana, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)

_, contours, _ = cv2.findContours(imUmb, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#dibuja borde
for c in contours:
    print(c);
    area = cv2.contourArea(c)
    if area > 1000 and area < 1000000:
        cv2.drawContours(mediana, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

plt.subplot(222), plt.imshow(imUmb), plt.title('bordes')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(mediana), plt.title('rectangulo')
plt.xticks([]), plt.yticks([])


#dibuja recuadro
"""for c in contours:
     area = cv2.contourArea(c)
     #retocar area minima y maxima posible
     if area > 1000 and area < 1000000:
         (x, y, w, h) = cv2.boundingRect(c)
         cv2.rectangle(mediana, (x, y), (x + w, y + h), (255, 0, 0), 1, cv2.LINE_AA)"""

plt.subplot(224), plt.imshow(contours), plt.title('rectangulo')
plt.xticks([]), plt.yticks([])

plt.show()
