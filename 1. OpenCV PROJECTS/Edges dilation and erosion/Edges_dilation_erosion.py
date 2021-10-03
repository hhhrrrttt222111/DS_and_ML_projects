import cv2 as c
import numpy as np
def graysc(img):
    imgray=c.cvtColor(img,c.COLOR_BGR2GRAY)
    c.imshow("Grayscale",imgray)
    c.waitKey(0)
def blur(img):
    imgblur=c.GaussianBlur(img,(15,15),0)
    c.imshow("Blur",imgblur)
    c.waitKey(0)
def edged(img):
    imgc=c.Canny(img,200,200)
    c.imshow("Edged",imgc)
    c.waitKey(0)
def diler(img,kernel):
    imgd=c.dilate(img,kernel=kernel,iterations=1)
    imge=c.erode(img,kernel=kernel,iterations=1)
    c.imshow("Dilated",imgd)
    c.imshow("Eroded",imge)
    c.waitKey(0)        
path="D:\OMEN\CR7.jpg"# insert the path of your image
img=c.imread(path)
kernel=np.ones((4,4),np.uint8)
diler(img,kernel)# call any function you want to


