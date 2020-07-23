import numpy as np
import cv2

ldrawing= False
rdrawing=False
ix,iy=-1,-1

def rect(event,x,y,flag,params):
    global ldrawing,ix,iy,rdrawing
    
    if event==cv2.EVENT_LBUTTONDOWN:
        ldrawing=True
        ix,iy=x,y
    if event==cv2.EVENT_RBUTTONDOWN:
        rdrawing=True
        ix,iy=x,y
    if event==cv2.EVENT_MOUSEMOVE:
        if ldrawing==True:
            cv2.rectangle(img,(x,y),(ix,iy),(255,0,0),-1)
        if rdrawing==True:
             cv2.rectangle(img,(x,y),(ix,iy),(0,0,0),-1)
    if event==cv2.EVENT_LBUTTONUP or event==cv2.EVENT_RBUTTONUP:
        if ldrawing==True:
            ldrawing=False
        if rdrawing==True:
            rdrawing=False
img=np.zeros(shape=(512,512,3),dtype=np.int8)

cv2.namedWindow('drawing')

cv2.setMouseCallback('drawing',rect)

while True:
    cv2.imshow('drawing',img)
    
    if cv2.waitKey(1) & 0xFF ==27:
        break
cv2.closeAllWindows()
    

            