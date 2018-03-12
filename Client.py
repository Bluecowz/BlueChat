import socket
from threading import Thread
from tkinter import END


class BlueClient:

    def __init__(self, server_ip, username):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._port = 10000
        self._server_IP = server_ip
        self._username = username

    def message_recv(self):
        try:
            data = self._sock.recv(4096)
            if data:
                return data.decode()
        except ConnectionAbortedError:
            print("Client Connection to was aborted.")

    def run_client(self):
        try:
            self._sock.connect((self._server_IP, self._port))
            # print("Connected...")
            # thread = Thread(target=self.message_recv, args=(self._sock,))
            # thread.start()
        except ConnectionResetError:
            self._sock.close()
            print("Connection was closed.")

    def close_client(self):
        self._sock.send((self._username + " disconnected.").encode())
        self._sock.close()

    def send_message(self, message):
        message = self._username + ": " + str(message)
        try:
            self._sock.send(message.encode())
        finally:
            pass



