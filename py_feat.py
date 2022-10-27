from time import sleep
from feat import Detector
from feat.utils import read_feat
import matplotlib.pyplot as plt
import pandas as pd
from feat.plotting import imshow
import cv2
import ctypes # An included library with Python install. ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='svm', #'svm' au_model='svm', emotion_model='jaanet'
    emotion_model="fer", #resmasknet
    facepose_model="img2pose",
)

multi_face_prediction = detector.detect_image("c1.png")

multi_face_prediction
detector.detect_image("c1.png", outputFname = "output.csv")

multi_face_prediction.plot_detections()
multi_face_prediction.emotions.plot.barh(y=None)

data=pd.read_csv("output.csv")
print(data[['fear','happiness','sadness','surprise','neutral','anger']])
df = data[['fear','happiness','sadness','surprise','neutral','anger']].copy()

max=data.iloc[0,0]
print(data['fear'].dtype)
maxValueIndex = df.idxmax(axis=1)
 
print("Emotion detected :"+ maxValueIndex)
case=maxValueIndex[0]
print(case[0])
if (case =='happiness'):
    ctypes.windll.user32.MessageBoxW(0, " Because of your smile, you make life more beautiful." , "Info", 1)
elif case== 'neutral':
    ctypes.windll.user32.MessageBoxW(0, " Let's put a smile on this face, shall we?" , "Info", 1)
elif case == 'sadness':
    ctypes.windll.user32.MessageBoxW(0, " WHY so SAD :( ?" , "Info", 1)
elif case=='surprise':
    ctypes.windll.user32.MessageBoxW(0, " :O " , "Info", 1)
else: #case 'fear':
    ctypes.windll.user32.MessageBoxW(0, " chill .." , "Info", 1)
      
            
plt.show()