import socket
import time
from threading import Thread


class Server:

    def __init__(self, given_ip=None):
        if given_ip is None:
            self._ip = '127.0.0.1'
        else:
            self._ip = given_ip
        self._port = 10000
        self._clients = set()

    def run_server(self):
        server_address = (self._ip, self._port)
        self.output_log("Set server IP and port")

        # Creates the socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.output_log("Socket created: " + str(self._ip) + ":" + str(self._port))

        try:
            sock.bind(server_address)
            sock.listen(5)

            while True:
                # Accept new connection
                connection, client_address = sock.accept()
                self.output_log("Accepted new connection")
                self._clients.add(connection)

                try:
                    thread = Thread(target=self.handle_connection, args=(connection,))
                    thread.start()
                except InterruptedError:
                    print("Threading error.")
        finally:
            sock.close()

    @staticmethod
    def broadcast_client(message, client):
        try:
            client.sendall(message)
        except ConnectionResetError as e:
            print("Client Forced Disconnect.")

    def broadcast(self, message):
        for derp in self._clients:
            send = Thread(target=self.broadcast_client, args=(message, derp,))
            send.start()

    def handle_connection(self, client):
        try:
            while True:
                time.sleep(10)
                data = client.recv(4096)
                if data:
                    derp = Thread(target=self.broadcast, args=(data,))
                    derp.start()
                    print("Data Received: " + data.decode())
                else:
                    pass
        except ConnectionError or ConnectionResetError as e:
            print("Error in handle_connection: " + str(e))

    @staticmethod
    def output_log(message):
        print(message)

