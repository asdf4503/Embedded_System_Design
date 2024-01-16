from socket import *
from gpiozero import LED
led = LED(17)
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)
connectionSock, addr = serverSock.accept()
print(str(addr),' connected')
while True:
    try:
        data = connectionSock.recv(1024).decode()
        print('rcv data :',data)
        if not data:
            break
        if data == '1':
            led.on()
        if data == '0':
            led.off()
    except KeyboardInterrupt:
        connectionSock.close()