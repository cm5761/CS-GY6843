# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverPort = 6789
  serverSocket.bind(("", serverPort))
  serverSocket.listen(1)

  while True:
    print'Ready to serve...'
    connectionSocket, addr = serverSocket.accept() 
    try:
    message =  connectionSocket.recv(1024)
    print(message,’::’), message.split()[0], ‘:’, message.split()[1]
    filename = message.split()[1]
    print(filename), ‘||’ , filename[1:]
    f = open(filename[1:])
    outputdata = f.read()
    connectionSocket.send(‘\nHTTP/1.1 200 OK\n\n’)
    
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i].encode())

    connectionSocket.send("\r\n".encode())
    connectionSocket.close()
  except IOError:
    connectionSocket.send(‘HTTP/1.1 404 Not Found\r\n’)
    connectionSocket.send("<html><head></head><body>404 Not Found</body></html>\r\n")
  connectionSocket.close()

