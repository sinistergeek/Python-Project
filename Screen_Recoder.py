import cv2
import numpy as np
from PIL import ImageGrab
import time

def screenrecoder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    name = int(round(time.time() * 1000))
    name = '{}.avi'.format(name)
    out = cv2.VideoWriter(name,fourcc,5.0,(1920,1080))

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recoder",frame)
        out.write(frame)
        if cv2.waitKey(1) == 27:
            break
out.release()
cv2.destroyAllWindows()
screenrecorder()
