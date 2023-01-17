# Import socket module
from socket import * 
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
#Fill in start
port= 56022;
Format = "UTF-8";
#SERVER =  "localHost"   #gethostbyname(gethostname())
socketAddr = ('', port)
serverSocket.bind(socketAddr)
serverSocket.listen()

while True:
	
	print('The server is ready to receive')
	
	connectionSocket, addr = serverSocket.accept()

	try:

		message = connectionSocket.recv(1024)
		#Fill in start             #Fill in end
		filename = message.split()[1]
		f = open(filename[1:])

		outputdata = f.read() #in start             #Fill in end
		
		# send one http header line in to the socket

		#Fill in start
		
		connectionSocket.send("HTTP/1.1 200 ok\r\n Content-Type: text/html\r\n\"".encode())
		#Fill in end
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		connectionSocket.close()

	except IOError:
			# Send HTTP response code and message for file not found
			#Fill in start
			notFound = "HTTP/1.1 404 FileNotFound\r\n\r\n"
			connectionSocket.send(notFound.encode())
			#Fill in end
			connectionSocket.send(bytes("<html><head></head><body><h1>404 File Not Found</h1></body></html>\r\n", Format))
			# Close the client connection socket
			#Fill in start
			connectionSocket.close()
			#Fill in end

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data

