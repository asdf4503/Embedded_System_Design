from gpiozero import Robot
import RPi.GPIO as GPIO
import time

dc_motor = Robot(left=(6, 12), right=(11, 9))

GPIO.setmode(GPIO.BCM)
button_pin = 27
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

motor_running = False

def button_callback(channel):
    global motor_running
    if not motor_running:
        motor_running = True
        dc_motor.forward(speed=1)
    else:
        motor_running = False
        dc_motor.stop()

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
