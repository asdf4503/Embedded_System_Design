import tkinter as tk
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

# TonalBuzzer 인스턴스를 생성합니다. GPIO 핀 17번을 사용합니다.
piezo = TonalBuzzer(4)

# 특정 톤을 연주하는 함수입니다.
def play_tone(tone):
    if tone == 'Stop':
        piezo.stop()
    else:
        piezo.play(Tone(tone))

# GUI 창을 초기화합니다.
root = tk.Tk()
root.title("Tone Generator")

# 음계에 따라 버튼을 생성하고 함수에 연결합니다.
tones = {
    'Do1': 262,
    'Re1': 294,
    'Mi1': 330,
    'Fa1': 349,
    'Sol1': 392,
    'La1': 440,
    'Si1': 494,
    'Do2': 523,
    'Re2': 587
}

# 버튼을 생성하고 화면에 배치합니다.
for note, freq in tones.items():
    button = tk.Button(root, text=note, command=lambda f=freq: play_tone(f))
    button.pack(side=tk.LEFT)

# 'Stop' 버튼을 추가합니다.
stop_button = tk.Button(root, text='Stop', command=lambda: play_tone('Stop'))
stop_button.pack(side=tk.LEFT)

# GUI를 실행합니다.
root.mainloop()
