# Note: Cameras are synch with threads used in CameraStream class
import cv2
import numpy as np
from camera_stream import CameraStream

displayWidth = 640
displayHeight = 480

# Laptop camera declaration
LAPTOP_CAM_CODE = 0
cam1 = CameraStream(LAPTOP_CAM_CODE, displayWidth, displayHeight)

# Webcam camera declaration
WEB_CAM_CODE = 1
cam2 = CameraStream(WEB_CAM_CODE, displayWidth, displayHeight)

while True:
  try: # try the program again if it has trouble when reading frames
    frame1 = cam1.getFrame()
    frame2 = cam2.getFrame()
    combinedFrame = np.hstack((frame1, frame2))
    cv2.imshow("Laptop Camera and Webcam Camera", combinedFrame)
    cv2.moveWindow("Laptop Camera and Webcam Camera", 0, 0)
  except:
    print("Frame not available: Trying to reconnect")
    
  # Option to exit the program gracefully
  if cv2.waitKey(1) == ord('q'):
    # release camera
    cam1.capture.release()
    cam2.capture.release()
    cv2.destroyAllWindows()
    exit(1) # killing all threads
    break
    