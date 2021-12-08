#Author: Armando Flores
#import socket module
#This programming assignment will teach me about socket programming connecting two nodes to have a client and server relationship
#In order to terminate program
from socket import *
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM) #AF_NET is for IPV4 and SOCKET_STREAM is used for TCP
    #print("Socket has been created!")
    #my_hostname = gethostname() #This returns the hostname of the current python interpreter is running on
    #ip_add = gethostbyname(my_hostname) #This will take the hostname and acquire the IP address of the host
    #print("This is ipv4 addi", {ip_add})
    #Prepare Server Socket
    #serverSocket.bind(( ip_add,port)) #We will bind this server to a specific port and host ipv4 address
    serverSocket.vind(("", port))
    serverSocket.listen(1) #The http server will be listening to incoming request
    #The 2 means that 2 other connections are kept waiting if theres a 3rd it will be dropped
    #print("Socket will be listening to incoming HTTP Request:")
    while True:
        #Establish the connection with the client requesting
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #connectionSocket is an object that allows me to send information to the connected Client
        #print("Got Connection from", addr)
        try:
            try:
                message = connectionSocket.recv(1024).decode('utf-8') # this will allow me to receive the message that client
                
                
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                

                #Send one HTTP header line into socket.
                successful_request = 'HTTP/1.1 200 OK\n'
                
                connectionSocket.send(successful_request.encode()) # the string will be converted to bytes before sent

                #Send the content of the requested file to the client

                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())


                connectionSocket.send("\r\n".encode())
                connectionSocket.close()

            except IOError :
                #print sys.exc_type
                failed_request = "HTTP/1.1 404 Not found\r\n\r\n" # this is the failed to find the requested hmtl document message
                connectionSocket.send(failed_request.encode())
                output = "<p>Error: Page Not Found<p>"
                connectionSocket.send(output.encode())
                connectionSocket.send("\r\n".encode())

                #Sending the header to the connection Socket client

                #Close client socket
                connectionSocket.close()
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit() #Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
  