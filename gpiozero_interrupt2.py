from gpiozero import Button, LED
from signal import pause

led1 = LED(17)

def go():
    led1.toggle()

button = Button(27)
button.when_pressed = go

pause()
