import cv2
import detector.py

video_name = "tokyo.mp4"
capture = cv2.VideoCapture(video_name)

i=0
while(capture.isOpened()):
    ret, frame = capture.read()
    if not ret:
        break
    print (i)
    i += 1

