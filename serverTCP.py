from socket import *
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready')
while True:
    connectionSocket, addr = serverSocket.accept()
    input = ''
    input = connectionSocket.recv(1024).decode()
    int_list = [int(i) for i in input.split()]
    print (int_list)
    sentence = ''
    for yr in int_list:
        if (yr%4) == 0 and (yr%100) != 0 or (yr%400) == 0:
            sentence = sentence + str(yr) + ' is a leap year\n'
        else:
            sentence = sentence + str(yr) + ' is not a leap year\n'
    connectionSocket.send(sentence.encode())
    connectionSocket.close()
