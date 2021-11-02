import hashlib
import socket
import select

MAX_MSG_LENGTH = 1024
port = 5555
ip = "127.0.0.1"


def print_client_sockets(client_sockets):
    for c in client_sockets:
        print("\t", c.getpeername())


def intput_cool_md5():
    md5_get = str(input("what the num?"))
    while int(len(md5_get)) > 10 or md5_get.isdecimal() == False:
        print("too much num-----------------or this is not only num")
        md5_get = str(input("what the num?"))
    return md5_get


md5_get = intput_cool_md5()
result = hashlib.md5(md5_get.encode())
md5hash = hashlib.md5()
print(result.hexdigest())

server_socket = socket.socket()
server_socket.bind((ip, port))
server_socket.listen()
print("Listening for clients...")
client_sockets = []
messages_to_send = []
while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
            print_client_sockets(client_sockets)
        else:
            data = current_socket.recv(MAX_MSG_LENGTH).decode()
            if data == "":
                print("Connection closed", )
                client_sockets.remove(current_socket)
                current_socket.close()
                print_client_sockets(client_sockets)
            else:
                messages_to_send.append((current_socket, data))
    for current_socket in wlist:
        current_socket.send(result.hexdigest().encode())

for message in messages_to_send:
    current_socket, data = message
    if current_socket in wlist:
        current_socket.send(data.encode())
        messages_to_send.remove(message)