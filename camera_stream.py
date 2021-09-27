from threading import Thread
import cv2 
import time

# Task for the class: The class will have a thread that constantly gathering frames
# 1. launch a camera -> do it one time, hence create a constructor for this
# 2. collect frames
# 3. allow user to get a frame from the launched camera
class CameraStream:
  def __init__(self, cameraSrc:int, width:int, height:int):
    self.width = width # width of display window
    self.height = height # height of display window
    self.capture = cv2.VideoCapture(cameraSrc) # launched the camera
    self.thread = Thread(target=self.update, args=()) # launched the thread that will continuously collects frame
    self.thread.daemon = True # kills the thread when the program is terminated
    self.thread.start() # start thread during initialization
    
  def update(self): # the class method will continuously reading frames from the passed camera
    while True:
      _, self.frame = self.capture.read()
      self.newFrame = cv2.resize(src = self.frame, dsize=(self.width, self.height)) # resize window to the given dimension
      
  def getFrame(self):
    return self.newFrame # return the new frame that has been resized
  