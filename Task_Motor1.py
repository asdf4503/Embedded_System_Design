from gpiozero import Robot
import tkinter as tk

dc_motor = Robot(left=(6, 12), right=(11, 9))

app = tk.Tk()
app.title("Motor Speed Control")

def set_motor_speed(speed):
    dc_motor.value = (speed, speed)

speed_slider = tk.Scale(app, from_=0, to=1, resolution=0.01, orient="vertical")
speed_slider.pack()

def slider_changed(event):
    speed = speed_slider.get()
    set_motor_speed(speed)

speed_slider.bind("<Motion>", slider_changed)

app.geometry("500x200")
app.mainloop()
