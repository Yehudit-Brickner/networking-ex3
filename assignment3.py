#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

SERVER_ADDRESS = ('0.0.0.0', 13000) # create a socket that is listing to all ips
serverSocket.bind(SERVER_ADDRESS) # binding the socket with the port
serverSocket.listen(1) # telling the socket to listen for 1 request at a time

while True:
    #Establish the connection
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept() # connecting with a client

    try:

        message = connectionSocket.recv(1024) # getting the request message form the client
        filename = message.split()[1] # getting the filename from the message
        f = open(filename[1:]) # opening the file statrting from the 2nd char in the name (the name starts with \ and we dont want that)
        outputdata = f.read() # the data we want to return in the file
        print(outputdata)
        # Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode()) # sending a message saying we got the request and were able to acsses the file        
               
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError :
        print("exception caught")

        #Send response message for file not found
        connectionSocket.send("\nHTTP/1.1 404 Not Found\r\n\r\n".encode())# sending a response saying we weren't able to accses the file
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body><html>\r\n".encode())
       
        #Close client socket
        connectionSocket.close()
        


serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    

