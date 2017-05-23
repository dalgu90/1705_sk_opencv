import cv2
import numpy as np

# TODO: In this practice, you track the woman skater in a video using one of the various trackers of OpenCV
#       and draw the result in rectangulars

# Open a video and Read the first frame
in_fpath = "videos/skating.mp4"

# Open a video and grad the first frame
v_in = cv2.VideoCapture(in_fpath)
ret, frame = v_in.read()
if not ret:
    print 'Cannot read video file'
    sys.exit()

# Define an initial bounding box(c, r, w, h)
bbox = (180, 95, 70, 100)  # videos/skating.mp4

# Set and initialize tracker.
# Use cv2.Tracker_create() method
# You can use MIL, BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN
############## YOUR CODE HERE ##############



############################################

while True:
    # Read a new frame
    ret, frame = v_in.read()
    if not ret:
        break

    # Update tracker and draw bounding box
    ############## YOUR CODE HERE ##############
    
    
    
    ############################################

    # Display result
    cv2.imshow("tracking", frame)
    
    # Wait a key press for 30ms
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break  # 'q' key to break

cv2.destroyAllWindows()
v_in.release()