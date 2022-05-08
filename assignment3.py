#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

SERVER_ADDRESS = ('0.0.0.0', 12000) # create a socket that is listing to all ips
serverSocket.bind(SERVER_ADDRESS) # binding the socket with the port
serverSocket.listen(1) # telling the socket to listen for 1 request at a time

while True:
    #Establish the connection
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept() # connecting with a client

    try:

        message = connectionSocket.recv(1024).decode() # getting the request message form the client
        # message = connectionSocket.recv(1024)
        print("printing message")
        print(message)
        print("finish printing message")

        filename = message.split()[1] # getting the filename from the message

        # if (filename[1:] == 'favicon.ico'): # we added this because it the server is getting another filena,e with this name after it gets the html file.
        #     continue

        f = open(filename[1:]) # opening the file statrting from the 2nd char in the name (the name starts with \ and we dont want that)
        outputdata = f.read() # the data we want to return in the file

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("200 OK\r\n".encode()) # sending a message saying we got the request and were able to acsses the file
        # Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError :
        print("exception caught")

        #Send response message for file not found
        #Fill in start
        connectionSocket.send("404 Not Found\r\n".encode()) # sending a response saying we weren't able to accses the file
        #Fill in end

        #Close client socket

        connectionSocket.close()
        # print("closed connectionSocket socket")


serverSocket.close()
# print("closed server socket")
sys.exit()#Terminate the program after sending the corresponding data                                    

