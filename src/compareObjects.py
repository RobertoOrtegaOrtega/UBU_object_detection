import cv2
from matplotlib import pyplot as plt

imagen1 = cv2.imread('faseFinal.png')
imagen2 = cv2.imread('faseFinal.png')
imagenAux1=cv2.absdiff(imagen1,imagen2)
cv2.imwrite('aux6.png',imagenAux1)

plt.subplot(421), plt.imshow(imagen1), plt.title('fase Final')
plt.xticks([]), plt.yticks([])
plt.subplot(422), plt.imshow(imagen2), plt.title('fase Final')
plt.xticks([]), plt.yticks([])

imagenGris1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
imagenGris2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

mediana1 = cv2.blur(imagenGris1, (20,20))
mediana2 = cv2.blur(imagenGris2, (20,20))
imgDiff=cv2.absdiff(mediana1,mediana2)

imUmb1 = cv2.adaptiveThreshold (mediana1, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)
imUmb2 = cv2.adaptiveThreshold (mediana2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)
imUmb3 = cv2.adaptiveThreshold (imgDiff, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)


_, contours1, _ = cv2.findContours(imUmb1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
_, contours2, _ = cv2.findContours(imUmb2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
_, contornoDiff, _ = cv2.findContours(imUmb3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#dibuja borde
for c in contours1:
    area = cv2.contourArea(c)
    if area > 1000 and area < 1000000:
        cv2.drawContours(mediana1, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
for c in contours2:
    area = cv2.contourArea(c)
    if area > 1000 and area < 1000000:
        cv2.drawContours(mediana2, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

for c in contornoDiff:
    area = cv2.contourArea(c)
    if area > 1000 and area < 1000000:
        cv2.drawContours(imgDiff, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

plt.subplot(423), plt.imshow(imUmb1), plt.title('bordes 1')
plt.xticks([]), plt.yticks([])
plt.subplot(424), plt.imshow(imUmb2), plt.title('bordes 2')
plt.xticks([]), plt.yticks([])

plt.subplot(425), plt.imshow(mediana1), plt.title('rectangulo')
plt.xticks([]), plt.yticks([])
plt.subplot(426), plt.imshow(mediana2), plt.title('rectangulo')
plt.xticks([]), plt.yticks([])
plt.subplot(427), plt.imshow(imUmb3), plt.title('objetos restantes')
plt.xticks([]), plt.yticks([])
plt.subplot(428), plt.imshow(imagenAux1), plt.title('objetos restantes')
plt.xticks([]), plt.yticks([])
plt.show()
