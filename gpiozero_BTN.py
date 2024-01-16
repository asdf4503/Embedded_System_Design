from gpiozero import LED
from tkinter import *

led = LED(17)

# Function
def led_on():
    led.on()

def led_off():
    led.off()

def led_blink():
    blink_on_time = float(on_time_entry.get())
    blink_off_time = float(off_time_entry.get())
    led.blink(on_time = blink_on_time, off_time = blink_off_time)

# Main
root = Tk()
root.geometry("800x150")
root.title("LED ON_OFF")

edtFrame = Frame(root)
edtFrame.pack()

btn_BLINK = Button(edtFrame, text = "LED_BLINK", command = led_blink)
btn_BLINK.pack(side = LEFT, padx = 10, pady = 10)

btn_ON = Button(edtFrame, text = "LED_ON", command = led_on)
btn_ON.pack(side = LEFT, padx = 10, pady = 10)

btn_OFF = Button(edtFrame, text = "LED_OFF", command = led_off)
btn_OFF.pack(side = LEFT, padx = 10, pady = 10)

entryFrame = Frame(root)
entryFrame.pack()

btn_on_time = Button(entryFrame, text = "BLINK_ON_TIME", state = DISABLED)
btn_on_time.pack(side = LEFT, padx = 10, pady = 10)

on_time_entry = Entry(entryFrame)
on_time_entry.pack(side = LEFT, padx = 10, pady = 10)

btn_off_time = Button(entryFrame, text = "BLINK_OFF_TIME", state = DISABLED)
btn_off_time.pack(side = LEFT, padx = 10, pady = 10)

off_time_entry = Entry(entryFrame)
off_time_entry.pack(side = LEFT, padx = 10, pady = 10)

#first setting
on_time_entry.insert(0, "2")
off_time_entry.insert(0, "2")

root.mainloop()
