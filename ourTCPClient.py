from socket import *


serverName = 'localhost'
serverPort = 13000
SERVER_ADDRESS = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(SERVER_ADDRESS)

sentence = input('Input html filename:')
print(sentence)
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(4096)

print('From Server:', modifiedSentence.decode())

clientSocket.close()