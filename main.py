# Note: Cameras are synch with threads used in CameraStream class
import cv2
import numpy as np
import time
from camera_stream import CameraStream
# lowpass filter constants
DELTA_T_AVERAGE_WEIGHT = 0.9
DELTA_T_WEIGHT = 0.1
deltaTimeAverage = 0

# display constants
displayWidth = 640
displayHeight = 480

# Laptop camera declaration
LAPTOP_CAM_CODE = 0
cam1 = CameraStream(LAPTOP_CAM_CODE, displayWidth, displayHeight)

# Webcam camera declaration
WEB_CAM_CODE = 1
cam2 = CameraStream(WEB_CAM_CODE, displayWidth, displayHeight)

# setup to display timer in the display window
font = cv2.FONT_HERSHEY_SIMPLEX
startTime = time.time() # calculate starting time


while True:
  try: # try the program again if it has trouble when reading frames
    frame1 = cam1.getFrame()
    frame2 = cam2.getFrame()
    combinedFrame = np.hstack((frame1, frame2))

    currentTime = time.time() # get the current time in the loop
    deltaTime = currentTime - startTime # calculate the time required to complete the task of getting frames from multi-camera
    startTime = time.time() # update the value of startTime
    
    # Setting up lowpass filter to not trust the collected data in the case then the deltaTime recorded is too big/slow
    # hence, setting up 10% weight of the deltaTime
    deltaTimeAverage = DELTA_T_AVERAGE_WEIGHT*deltaTimeAverage + DELTA_T_WEIGHT*deltaTime 
    
    # calculate fps
    fps = round(1/deltaTimeAverage, 1) # frame persecond will be calculated using the lowpass filtered change of time
    cv2.rectangle(combinedFrame, (0,0), (150, 40), (0,0,0), -1)
    cv2.putText(combinedFrame, str(fps)+" FPS", (10, 25), font, 0.75, (255, 255, 255))
    cv2.imshow("Laptop Camera and Webcam Camera", combinedFrame)
    # print(f"Reading Time: {deltaTimeAverage} seconds")
  except:
    print("CameraStream not available: Trying to reconnect")
    
  # Option to exit the program gracefully
  if cv2.waitKey(1) == ord('q'):
    # release camera
    cam1.stopStreamThread()
    cam1.release()
    
    cam2.stopStreamThread()
    cam2.release()
    cv2.destroyAllWindows()
    exit(1) # killing all threads
    breakpython --version
    
    