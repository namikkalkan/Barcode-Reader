import cv2
import numpy as np
from pyzbar import pyzbar

# pyzbar gives many information data, type, shape
#now for multiple
#img = cv2.imread('download.png')
#cap.set (3,640) #3 is id for weight
#cap.set(4,480)  #4 is id for height

cap = cv2.VideoCapture(0)

with open ('data_file.txt') as f:
        data_list = f.read().splitlines()
        print(data_list)

while True:
        success,img = cap.read()
        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
                # barcode.data give byte'1111'
                mydata = barcode.data.decode('utf-8')
                print(mydata) # now it is just data
                if mydata in data_list:
                        output = f' "{mydata}" Stored in Database'
                        color = (0,0,255)
                else :
                        output = f' "{mydata}" New Barcode'
                        color = (255, 255,0)
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts], True,color,5)
                cv2.putText(img,output,(50,200),
                fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                fontScale=1,
                color=color)
        cv2.imshow('result', img)
        keyCode = cv2.waitKey(1)
        if (keyCode & 0xFF) == ord("q"):
                cv2.destroyAllWindows()
                break


