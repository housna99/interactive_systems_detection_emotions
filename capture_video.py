import cv2

#Capture video from webcam
vid_capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

while(True):
     # Capture each frame of webcam video
     ret,frame = vid_capture.read()
     cv2.imshow("My cam video", frame)
     out.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break

# close the already opened camera
vid_capture.release()
# close the already opened file
out.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()