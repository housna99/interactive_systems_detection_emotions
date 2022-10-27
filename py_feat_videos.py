import time
from feat.utils import get_test_data_path
from IPython.core.display import Video
import matplotlib.pyplot as plt
from feat import Detector
from feat.utils import read_feat
import matplotlib.pyplot as plt
import pandas as pd
from feat.plotting import imshow
detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='svm',
    emotion_model="resmasknet",
    facepose_model="img2pose",
)
#--INFO : The frame is a single image in a sequence of pictures. In general, one second of a video is comprised of 24 or 30 frames per second also known as FPS.
# Frame 48 = ~0:02
# Frame 408 = ~0:14
test_data_dir = get_test_data_path()
#test_video_path = os.path.join(test_data_dir, "output.mp4")

# Show video
Video( "output.mp4", embed=False)
#prob de mémoire ! 
print("-- start detecting emotions, please hold !--")
start_time = time.time()

video_prediction = detector.detect_video( "output.mp4", skip_frames=24,outputFname = "output_video.csv")
print(video_prediction.head())
print(video_prediction.shape)
video_prediction.loc[[48,408]].plot_detections(faceboxes=False, add_titles=False)

plt.show()
video_prediction.emotions.plot()
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()

