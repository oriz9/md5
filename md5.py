import hashlib
import socket
import select
from MyNetwork import network_handler

class my_server:

    MAX_MSG_LENGTH = 1024
    port = 5555
    ip = "127.0.0.1"

    def __init__(self):
        self.md5_get = intput_cool_md5()
        self.result = hashlib.md5(self.md5_get.encode())
        md5hash = hashlib.md5()
        print(self.result.hexdigest())

        # network variables:
        self.server_socket = socket.socket()
        self.client_sockets = []

    def init_network(self):
        self.server_socket.bind((my_server.ip, my_server.port))
        self.server_socket.listen()
        print("Listening for clients...")

    def do_iteration(self):
        messsage_to_send = []
        rlist, wlist, xlist = select.select([self.server_socket] + self.client_sockets, self.client_sockets, [])
        for current_socket in rlist:
            if current_socket is self.server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                self.client_sockets.append(connection)
                print_client_sockets(self.client_sockets)
            else:
                data = current_socket.recv(my_server.MAX_MSG_LENGTH).decode()
                if data == "":
                    print("Connection closed", )
                    self.client_sockets.remove(current_socket)
                    current_socket.close()
                    print_client_sockets(self.client_sockets)
                else:
                    messsage_to_send.append((current_socket, data))
        for current_socket in wlist:
            current_socket.send(self.result.hexdigest().encode())


        for message in messsage_to_send:
            current_socket, data = message
            if current_socket in wlist:
                current_socket.send(data.encode())
                messsage_to_send.remove(message)

def print_client_sockets(client_sockets):
    for c in client_sockets:
        print("\t", c.getpeername())


def intput_cool_md5():
    md5_get = str(input("what the num?"))
    while int(len(md5_get)) > 10 or md5_get.isdecimal() == False:
        print("too much num-----------------or this is not only num")
        md5_get = str(input("what the num?"))
    return md5_get




def main():

    server = my_server()
    my_server.init_network()

    while True:
        server.do_iteration()


if __name__ == "__main__":
    main()