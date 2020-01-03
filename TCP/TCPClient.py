from socket import *
servername = '127.0.0.1'
serverport = 12000
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername, serverport))
sentence = input('input lowercase sentence:')
clientsocket.send(sentence.encode())
modifiedsentence = clientsocket.recv(1024)
print('from server:', modifiedsentence)
clientsocket.close()