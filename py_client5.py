from socket import *
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('localhost', 8080))
print('connection OK')
while True:
    try:
        command = input('Enter your command: ')
        if not command:  # If no command entered (empty string)
            break
        clientSock.send(bytes(command,'utf-8'))
        print('client : sent msg')
        #data = clientSock.recv(1024)
        # #print('recved data:',data)
    except KeyboardInterrupt:
        pass
clientSock.close()