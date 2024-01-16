import tkinter as tk
import serial
port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)

# 특정 톤을 연주하는 함수
def play_tones(tones):
	tones = tones.encode('utf-8')
	print(tones)
	arduino.write(tones)

# GUI 창 초기화
root = tk.Tk()
root.title("Tone Generator")

# 음계에 따라 버튼을 생성하고 함수에 연결
tones = {
    'Do1': '1',
    'Re1': '2',
    'Mi1': '3',
    'Fa1': '4',
    'Sol1': '5',
    'La1': '6',
    'Si1': '7',
    'Stop': '0',
}

# 버튼 생성 및 화면 배치
for note, freq in tones.items():
    button = tk.Button(root, text=note, command=lambda f=freq: play_tones(f))
    button.pack(side=tk.LEFT)

# GUI 실행
root.mainloop()
