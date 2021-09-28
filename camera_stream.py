from threading import Thread, Lock
import cv2 

# Task for the class: The class will have a thread that constantly gathering frames
# 1. launch a camera -> do it one time, hence create a constructor for this
# 2. collect frames
# 3. allow user to get a frame from the launched camera
class CameraStream:
  def __init__(self, cameraSrc:int, width:int, height:int):
    self._width = width # width of display window
    self._height = height # height of display window
    self._capture = cv2.VideoCapture(cameraSrc) # launched the camera
    self._threadStarted = True
    self._thread = Thread(target=self._update, args=()) # launched the thread that will continuously collects frame
    self._readLock = Lock()
    self._thread.daemon = True # kills the thread when the program is terminated
    self._thread.start() # start thread during initialization

  # private method that only used within the class
  def _update(self): # the class method will continuously reading frames from the passed camera
    while self._threadStarted:
      _, self._frame = self._capture.read()
      self._readLock.acquire()
      self._newFrame = cv2.resize(src = self._frame, dsize=(self._width, self._height)) # resize window to the given dimension
      self._readLock.release()
  
  def getFrame(self): return self._newFrame # return copy of the new frame that has been resized
  
  def stopStreamThread(self):
    self._threadStarted = False
    self._thread.join()
  
  def release(self):
    self._capture.release()