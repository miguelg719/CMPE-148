from socket import *
serverName = 'localhost'
serverPort = 10000
serverAdress = (serverName, serverPort)
sock = socket(AF_INET, SOCK_DGRAM)
print("connecting to", serverName, ";", serverPort)

total = ""
with open('years.txt') as years:
    for line in years:
        total += line;
    sent = sock.sendto(total.encode(), serverAdress)
    result, address = sock.recvfrom(4096)
    print ("total = " + result.decode())
    sock.close()
