import cv2
import numpy as np
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def mouseAction(event, x, y, flag, a):
    if event == cv2.EVENT_LBUTTONDOWN:
        if (x >= 50 and x<=250) and (y >= 50 and y<=250):
            print("mouse left button click: GREEN BOX click")
            print(f"location {x}:{y}")
            GPIO.output(23, not GPIO.input(23))
        elif (x >= 350 and x<=550) and (y >= 50 and y<=250):
            print("mouse left button click: RED BOX click")
            print(f"location {x}:{y}")
            GPIO.output(24, not GPIO.input(24))
        else:
            print("mouse left button click: OTHER AREA click")
            print(f"location {x}:{y}")
            GPIO.output(23, False)
            GPIO.output(24, False)

img = np.zeros((300, 600, 3), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (250, 250), color=(0, 255, 0), thickness=-1)  # GREEN
cv2.rectangle(img, (350, 50), (550, 250), color=(0, 0, 255), thickness=-1)  # RED
cv2.imshow("image", img)
cv2.setMouseCallback('image', mouseAction)

cv2.waitKey(0)
cv2.destroyAllWindows()
GPIO.cleanup()
