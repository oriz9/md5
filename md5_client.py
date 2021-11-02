import socket
my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 5555))
data = my_socket.recv(1024).decode()
print("The server sent " + data)
while True:
    pass