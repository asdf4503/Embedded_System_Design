from gpiozero import Button, LED
from time import sleep
from signal import pause
led1 = LED(17)
led2 = LED(18)
button = Button(27)
def go():
    print("Button is pressed")

led1.blink(on_time = 0.5, off_time = 0.5)
led2.blink(on_time = 1, off_time = 1)
button.when_pressed = go

pause()