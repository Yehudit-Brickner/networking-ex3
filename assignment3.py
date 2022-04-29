#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
SERVER_ADDRESS = ('0.0.0.0', 13000)
serverSocket.bind(SERVER_ADDRESS)
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept()
    print("made a connection")
    #Fill in end


    try:
        print("im in the try")
    #     #Fill in start
    #     message = input('please enter a file name')
    #     #Fill in end
    #     filename = message.split()[1]
    #     f = open(filename[1:])
    #     #Fill in start
    #     outputdata =
    #     #Fill in end
    #
    #     #Send one HTTP header line into socket
    #     #Fill in start
    #     #Fill in end
    #
    #     #Send the content of the requested file to the client
    #     for i in range(0, len(outputdata)):
    #         connectionSocket.send(outputdata[i].encode())
    #     connectionSocket.send("\r\n".encode())
    #
    #     connectionSocket.close()
    except IOError:
        print("exception caught")
        #Send response message for file not found
        #Fill in start
        # connectionSocket.send(bytes("404 Not Found"))
        #Fill in end

        #Close client socket
        #Fill in start
        # clientSocket.close()
        # print("closed client socket")
        #Fill in end

serverSocket.close()
print("closed server socket")
sys.exit()#Terminate the program after sending the corresponding data                                    

