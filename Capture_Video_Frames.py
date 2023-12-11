import os
import shutil
import sys
import cv2

class FrameCapture:
    def __init__(self,file_path):
        self.directory = "captured_frames"
        self.file_path = file_path

        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)
