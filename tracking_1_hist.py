import os
import numpy as np
import cv2 # OpenCV-Python

# TODO: Description

# Open a video
in_fpath = "videos/basketball.mp4"
#in_fpath = "videos/walking.mp4"
v_in = cv2.VideoCapture(in_fpath)

# take first frame of the video
ret, frame = v_in.read()

# setup initial location of window(simply hardcoded the values)
c, r, w, h = (187, 218, 45, 100)
#c, r, w, h = (530, 300, 30, 60)
track_window = (c, r, w, h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((40., 50.,50.)), np.array((80.,255.,255.)))  # Select only green-ly pixels
#mask = cv2.inRange(hsv_roi, np.array((0., 0.,0.)), np.array((179.,255.,50.)))  # Black pixels?
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [20], [0,180])  # Calculates a histogram of Hue values
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while True:
    ret ,frame = v_in.read()
    
    # Uncomment this lines to see the track_window is set well
    #img2 = cv2.rectangle(frame, (c, r), (c+w,r+h), 255, 2)
    #cv2.imshow('meanshift',img2)
    #cv2.waitKey(100000)
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        #ret, track_window = cv2.CamShift(dst, track_window, term_crit)
                                          
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
        cv2.imshow('meanshift',img2)
        
        # Wait a key press for 60ms
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break  # 'q' key to break
    else:
        break

cv2.destroyAllWindows()
v_in.release()
