from gpiozero import Button, LED
from time import sleep
from signal import pause
from gpiozero import Robot

led1 = LED(17)
led2 = LED(18)
button = Button(27)
dc_motor = Robot(left=(6, 12), right=(11, 9))

motor_control = False

def go():
    global motor_control
    if not motor_control:
        dc_motor.forward(speed=1)
        motor_control = True

    else:
        dc_motor.stop()
        motor_control = False

led1.blink(on_time = 0.5, off_time = 0.5)
led2.blink(on_time = 1, off_time = 1)
button.when_pressed = go

pause()