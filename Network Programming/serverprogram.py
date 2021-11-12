import socket
s = socket.socket()
print("Socket successfully created")
port = 777
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)  # 5 incoming connections will be queued up
print("socket is listening")
while True:
    c, addr = s.accept()
    while True:
        print('Got connection from', addr, "\n Give your message\n")
        message = input()

        c.send(message.encode())
        message = c.recv(1024).decode()
        print("Received ", message)
    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
