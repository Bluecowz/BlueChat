import socket
from threading import Thread


def broadcast_client(message, client):
    client.sendall(message)


def broadcast(message):
    for derp in clients:
        send = Thread(target=broadcast_client, args=(message, derp,))
        send.start()


def handle_connection(client):
    try:
        while True:
            data = client.recv(4096)
            if data:
                derp = Thread(target=broadcast, args=(data,))
                derp.start()
                print("Data Received: " + data.decode())
            else:
                pass
            # time.sleep(10)
    except ConnectionError:
        print("Error in handle_connection.")


def output_log(message):
    print(message)


# Set the server IP
ip = input("Server IP: ")
if ip == "":
    ip = '127.0.0.1'
port = 10000

server_address = (ip, port)
output_log("Set server IP and port")

# Creates the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
output_log("Socket created: " + str(ip) + ":" + str(port))

clients = set()

try:
    # Bind the socket to the port and begins listening for connections
    sock.bind(server_address)
    sock.listen(5)

    while True:
        # Accept new connection
        connection, client_address = sock.accept()
        output_log("Accepted new connection")
        clients.add(connection)

        try:
            thread = Thread(target=handle_connection, args=(connection,))
            thread.start()
        except InterruptedError:
            print("Threading error.")


finally:
    sock.close()






