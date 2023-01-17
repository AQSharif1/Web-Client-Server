from socket import * 
import sys

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]
socketAddrs = (server_host, server_port)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(socketAddrs)
clientMes = "GET " + '/' + str(filename) + " HTTP/1.1"
clientSocket.send(clientMes.encode())
clientResponse = clientSocket.recv(1024)

while (len(clientResponse)> 0):
    print(clientResponse.decode())
    clientResponse = clientSocket.recv(1024)
clientSocket.close()


