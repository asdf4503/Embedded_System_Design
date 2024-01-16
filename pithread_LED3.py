import RPi.GPIO as GPIO
import threading
import time

# GPIO 핀 설정
LED1_PIN = 17
LED2_PIN = 18
LED3_PIN = 27
BUTTON_PIN = 6

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀을 출력으로 설정
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)

# 버튼 핀을 입력으로 설정, 내부 풀다운 저항 활성화
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blink_led(pin, delay, times):
    """LED를 깜빡이는 함수"""
    for _ in range(times):
        GPIO.output(pin, True)
        time.sleep(delay)
        GPIO.output(pin, False)
        time.sleep(delay)

def keyboard_input_listener():
    """키보드 입력을 감지하여 LED1을 깜빡이는 함수"""
    while True:
        input("Press Enter to blink LED1: ")  # 키보드 입력 대기
        blink_led(LED1_PIN, 0.5, 3)

def button_input_listener():
    """버튼 입력을 감지하여 LED2를 깜빡이는 함수"""
    while True:
        # 버튼이 눌림을 감지
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING)
        blink_led(LED2_PIN, 0.2, 5)
        # 디바운싱을 위한 간단한 지연
        time.sleep(0.1)

def led3_blinker():
    """LED3를 무한히 깜빡이는 함수"""
    while True:
        GPIO.output(LED3_PIN, True)
        time.sleep(1)
        GPIO.output(LED3_PIN, False)
        time.sleep(1)

# 쓰레드 생성
t1 = threading.Thread(target=keyboard_input_listener)
t2 = threading.Thread(target=button_input_listener)
t3 = threading.Thread(target=led3_blinker)

# 쓰레드 시작
t1.start()
t2.start()
t3.start()