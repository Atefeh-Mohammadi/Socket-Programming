from socket import *
servername = '127.0.0.1'
serverport = 12000
clientsocket = socket(AF_INET, SOCK_DGRAM)
message = input('input lowercase sentence:')
clientsocket.sendto(message.encode(), (servername, serverport))
modifiedmessage, serveraddress = clientsocket.recvfrom(2048)
print(modifiedmessage)
clientsocket.close()