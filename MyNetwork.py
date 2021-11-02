from socket import socket

class network_handler:
    def __init__(self, s: socket):
        self.s = s

    def receive(self) -> bytearray:
        pass

    def send(self, data: bytearray):
        pass