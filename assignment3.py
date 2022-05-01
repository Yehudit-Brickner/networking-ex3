#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
SERVER_ADDRESS = ('0.0.0.0', 12000)
serverSocket.bind(SERVER_ADDRESS)
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept()
    print("made a connection with ", connectionSocket, addr)
    #Fill in end


    try:
        print("/nim in the try/n ")
        #Fill in start
        message = connectionSocket.recv(4096).decode()
        # print(message)
        #Fill in end
        filename = message.split()[1]
        if (filename[1:] == 'favicon.ico'):
            continue
        print(filename)
        f = open(filename[1:])
        #Fill in start
        outputdata = f.read()
        #Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\n".encode())
        # Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        print("exception caught")
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(bytes("404 Not Found\n"))
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        # print("closed client socket")
        #Fill in end

serverSocket.close()
print("closed server socket")
sys.exit()#Terminate the program after sending the corresponding data                                    

