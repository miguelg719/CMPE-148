from socket import *
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
serverAddress = ('localhost', serverPort)
print ('The server is ready')
while True:
    input = ''
    adress = ''
    input, address = serverSocket.recvfrom(4096)
    int_list = [int(i) for i in input.split()]
    print (int_list)
    sentence = ''
    for yr in int_list:
        if (yr%4) == 0 and (yr%100) != 0 or (yr%400) == 0:
            sentence = sentence + str(yr) + ' is a leap year\n'
        else:
            sentence = sentence + str(yr) + ' is not a leap year\n'
    sent = serverSocket.sendto(sentence.encode(), address)

serverSocket.close()
