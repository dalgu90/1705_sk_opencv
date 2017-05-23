import cv2
import numpy as np

# In this tutorial, we use various (comparatively) recent object trackers offered by OpenCV.

# Set up tracker.
# MIL, BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN
# (GOTURN need Caffe prototxt and finetuned caffemodel)
tracker = cv2.Tracker_create("KCF")

# Open a video and Read the first frame
in_fpath = "videos/basketball.mp4"
#in_fpath = "videos/walking.mp4"
#in_fpath = "videos/dog.mp4"

# Open a video and grad the first frame
v_in = cv2.VideoCapture(in_fpath)
ret, frame = v_in.read()
if not ret:
    print 'Cannot read video file'
    sys.exit()

# Define an initial bounding box(c, r, w, h)
bbox = (187, 218, 45, 100)  # videos/basketball.mp4
#bbox = (530, 300, 30, 60)  # videos/walking.mp4
#bbox = (180, 95, 70, 100)  # videos/dog.mp4

# Uncomment this lines to see the track_window is set well
#img2 = cv2.rectangle(frame, (bbox[0],bbox[1]), (bbox[0]+bbox[2],bbox[1]+bbox[3]), (0,0,255))
#cv2.imshow('tracking',img2)
#cv2.waitKey(100000)

# Initialize tracker with first frame and bounding box
ret = tracker.init(frame, bbox)

while True:
    # Read a new frame
    ret, frame = v_in.read()
    if not ret:
        break

    # Update tracker
    ret, bbox = tracker.update(frame)

    # Draw bounding box
    if ret:
        cv2.rectangle(frame, (int(bbox[0]),int(bbox[1])),
                      (int(bbox[0]+bbox[2]),int(bbox[1]+bbox[3])), (0,0,255))

    # Display result
    cv2.imshow("tracking", frame)
    
    # Wait a key press for 1ms
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break  # 'q' key to break

cv2.destroyAllWindows()
v_in.release()