import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

#config me here#
method = 2
################
################

#step = 100

color_white = (255,255,255)
color_black = (0,0,0)
color_gray = (128,128,128)

colors = [color_white,color_black,color_gray]

#input
image = np.zeros((600,300,3), dtype=np.uint8)

cv2.rectangle(image,(0,0),(100,100),color_white,-1)
cv2.rectangle(image,(0,100),(100,200),color_white,-1)
cv2.rectangle(image,(0,200),(100,300),color_white,-1)

cv2.rectangle(image,(0,300),(100,400),color_white,-1)
cv2.rectangle(image,(0,400),(100,500),color_white,-1)
cv2.rectangle(image,(0,500),(100,600),color_white,-1)


cv2.rectangle(image,(100,0),(200,100),color_gray,-1)
cv2.rectangle(image,(100,100),(200,200),color_gray,-1)
cv2.rectangle(image,(100,200),(200,300),color_gray,-1)

cv2.rectangle(image,(100,300),(200,400),color_gray,-1)
cv2.rectangle(image,(100,400),(200,500),color_gray,-1)
cv2.rectangle(image,(100,500),(200,600),color_gray,-1)


cv2.circle(image,(50,50),25,color_black,-1)
cv2.rectangle(image,(25,125),(75,175),color_black,-1)
a3 = np.array( [[[25,225],[25,275],[75,275]]], dtype=np.int32 )
cv2.fillPoly(image, a3,color_black)

cv2.circle(image,(50,350),25,color_gray,-1)
cv2.rectangle(image,(25,425),(75,475),color_gray,-1)
a3 = np.array( [[[25,525],[25,575],[75,575]]], dtype=np.int32 )
cv2.fillPoly(image, a3,color_gray)

cv2.rectangle(image,(125,125),(175,175),color_black,-1)
cv2.circle(image,(150,50),25,color_black,-1)
a3 = np.array( [[[125,225],[125,275],[175,275]]], dtype=np.int32 )
cv2.fillPoly(image, a3,color_black)

cv2.rectangle(image,(125,425),(175,475),color_white,-1)
cv2.circle(image,(150,350),25,color_white,-1)
a3 = np.array( [[[125,525],[125,575],[175,575]]], dtype=np.int32 )
cv2.fillPoly(image, a3,color_white)

cv2.circle(image,(250,50),25,color_white,-1)
cv2.rectangle(image,(225,125),(275,175),color_white,-1)
a3 = np.array( [[[225,225],[225,275],[275,275]]], dtype=np.int32 )
cv2.fillPoly(image, a3,color_white)

cv2.circle(image,(250,350),25,color_gray,-1)
cv2.rectangle(image,(225,425),(275,475),color_gray,-1)
a3 = np.array( [[[225,525],[225,575],[275,575]]], dtype=np.int32 )
cv2.fillPoly(image, a3,color_gray)

#cv2.rectangle(image,(200,0),(200,100),color_black,-1)
#cv2.rectangle(image,(200,100),(200,300),color_black,-1)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(image)
plt.show()

#plt.imshow(image)
#plt.show()

#doing

if method == 0:
    kernel1 = np.array([[-1/9, 0,1/9],[-1/9,0,1/9],[-1/9,0,1/9]])
    dst1 = cv2.filter2D(image, -1, kernel1)

    kernel2 = np.array([[-1/9, -1/9,-1/9],[0,0,0],[1/9,1/9,1/9]])
    dst2 = cv2.filter2D(image, -1, kernel2)
elif method == 1:
    kernel1 = np.array([[-1, 0,1],[-1,0,1],[-1,0,1]])
    dst1 = cv2.filter2D(image, -1, kernel1)

    kernel2 = np.array([[-1, -1,-1],[0,0,0],[1,1,1]])
    dst2 = cv2.filter2D(image, -1, kernel2)
elif method == 2:
    dst1 = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
    dst2 = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)


cv2.imshow(dst1, cmap = 'gray')
plt.show()
#cv2.waitKey(0)

plt.imshow(dst2, cmap = 'gray')
plt.show()

theNewImage = np.zeros((600,300,3), dtype=np.uint8)

for i in range(len(dst1)):
    for j in range(len(dst1[i])):
        theNewImage[i][j][0] = math.sqrt(dst1[i][j] ** 2 + dst2[i][j] ** 2)
        theNewImage[i][j][1] = dst1[i][j]
        theNewImage[i][j][2] = dst2[i][j]

plt.imshow(theNewImage)
plt.show()




#new pic
