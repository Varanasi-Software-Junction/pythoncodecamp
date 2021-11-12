# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 777

# connect to the server on local computer
c=s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
while True:
    print(s.recv(1024).decode())
    message=input()
    s.send(message.encode())

# close the connection
s.close()