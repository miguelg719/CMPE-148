from socket import *
serverName = 'localhost'
serverPort = 10000
sock = socket(AF_INET, SOCK_STREAM)
print("connecting to", serverName, ",", serverPort)
sock.connect((serverName, serverPort))
print("connected:", serverName, ",", serverPort)

total = ""
with open('years.txt') as years:
    for line in years:
        total += line;
    sock.send(total.encode())
    print ("total = " + sock.recv(1024).decode())
    sock.close()
