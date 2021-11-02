import socket


class internet:
    def __init__(self, sockket):
        self.my_socket = sockket

    def reciv(self):
        data = self.my_socket.recv(1024).decode()


internet(socket.socket())


