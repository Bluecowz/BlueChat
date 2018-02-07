import socket
from threading import Thread


def message_recv(connection):
    while True:
        data = connection.recv(4096)
        if data:
            print(data.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 10000
server_IP = input("Server IP: ")
username = input("Your Username: ")

try:
    sock.connect((server_IP, port))
    thread = Thread(target=message_recv, args=(sock,))
    thread.start()
    while True:
        message = input(">>> ")
        message = username + ": " + message
        try:
            sock.send(message.encode())
        finally:
            pass
except ConnectionResetError:
    sock.close()
    print("Connection was closed.")
finally:
    sock.send((username + " disconnected.").encode())
    sock.close()
