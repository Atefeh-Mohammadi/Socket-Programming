from socket import *
serverport = 12000
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverport))
print('server is ready to receive')
while True:
    message, clientaddress = serversocket.recvfrom(2048)
    modifiedmessage = message.upper()
    serversocket.sendto(modifiedmessage, clientaddress)