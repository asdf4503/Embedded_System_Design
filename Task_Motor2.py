from gpiozero import Robot
import tkinter as tk

dc_motor = Robot(left=(6, 12), right=(11, 9))

app = tk.Tk()
app.title("Motor Speed Controller")

current_speed = 0

def set_motor_speed(speed):
    dc_motor.value = (speed, speed)

speed_label = tk.Label(app, text="Motor Speed (0.1 - 0.9):")
speed_label.pack()

speed_entry = tk.Entry(app)
speed_entry.pack()
speed_entry.insert(0, current_speed)

def entry_return(event):
    new_speed = float(speed_entry.get())
    while(True) :
        set_motor_speed(new_speed)
        speed_entry.delete(0, tk.END)
        speed_entry.insert(0, current_speed)

speed_entry.bind("<Return>", entry_return)

set_motor_speed(current_speed)

app.mainloop()
