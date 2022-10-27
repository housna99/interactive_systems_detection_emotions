
from time import sleep
import cv2

#Capture video from webcam
cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
sleep(5)
 # return a single frame in variable `frame`


print('capturing image')
while(True):
    ret,frame = cap.read()
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('c1.png',frame)
        cv2.destroyAllWindows()
        break
    # elif cv2.waitKey(1) & 0xFF == ord('n'):
    #     cv2.destroyAllWindows()
    #  break
cap.release()
# close the window and de-allocate any associated memory usage
