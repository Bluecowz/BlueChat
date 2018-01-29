import socket
from threading import RLock
from threading import Thread


def handle_connection(client):
    try:
        while True:
            data = client.recv(4096)
            if data:
                lock.acquire()
                for x in clients:
                    x.sendall(data)
                print("Data Received: " + data.decode())
                lock.release()
            else:
                pass
            # time.sleep(10)
    except ConnectionError:
        print("Error in handle_connection.")


def output_log(message):
    print(message)


# Set the server IP
ip = "127.0.0.1"

port = 10000
server_address = (ip, port)
output_log("Set server IP and port")

# Creates the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
output_log("Socket created.")

clients = set()
lock = RLock()


try:
    # Bind the socket to the port and begins listening for connections
    sock.bind(server_address)
    sock.listen(5)

    while True:
        # Accept new connection
        connection, client_address = sock.accept()
        output_log("Accepted new connection")
        lock.acquire()
        clients.add(connection)
        lock.release()

        try:
            thread = Thread(target=handle_connection, args=(connection,))
            thread.start()
        except InterruptedError:
            print("Threading error.")


finally:
    sock.close()






