from gpiozero import Robot
import tkinter as tk
import sys
import threading

dc_motor = Robot(left=(6, 12), right=(11, 9))

app = tk.Tk()
app.title("Motor Speed Controller")

current_speed = 0

def update_motor_speed(speed):
    global current_speed
    current_speed = speed
    dc_motor.value = (speed, speed)

speed_label = tk.Label(app, text="Motor Speed (0.1 - 0.9):")
speed_label.pack()
speed_entry = tk.Entry(app)
speed_entry.pack()
speed_entry.insert(0, current_speed)

def entry_return(event):
    new_speed = float(speed_entry.get())
    if 0 <= new_speed <= 0.9:
        update_motor_speed(new_speed)

speed_entry.bind("<Return>", entry_return)

if len(sys.argv) > 1:
    initial_speed = float(sys.argv[1])
    if 0.1 <= initial_speed <= 0.9:
        update_motor_speed(initial_speed)
        speed_entry.delete(0, tk.END)
        speed_entry.insert(0, initial_speed)

def motor_control_thread():
    while True:
        speed = float(speed_entry.get())
        update_motor_speed(speed)

motor_thread = threading.Thread(target=motor_control_thread)
motor_thread.daemon = True
motor_thread.start()

app.mainloop()
