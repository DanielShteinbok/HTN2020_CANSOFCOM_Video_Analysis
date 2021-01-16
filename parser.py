import cv2
import time
import detector

video_name = "tokyo.mp4"
capture = cv2.VideoCapture(video_name)

def print_output(current_frame_val, current_timestamp, prev_frame_val=None):
    print(current_frame_val)
    #print(",\n")
    print(prev_frame_val)
    #print(",\n")
    print(current_timestamp)
    #print(",\n")

frame_count = 0
prev_frame_val = None
for i in range(1800):
    capture.read()
    frame_count += 1
    print(frame_count)

while(capture.isOpened()):
    ret, frame = capture.read()
    if not ret:
        break
    current_frame_val = detector.yolo_int(frame)
    frame_count += 1
    print_output(current_frame_val, frame_count, prev_frame_val)
    prev_frame_val = current_frame_val

