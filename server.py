import socket
from tic_tac_toe import TicTacToe


HOST=socket.gethostbyname(socket.gethostname())
PORT=8888
EXIT_MESSAGE="goodbye"
CLIENT_MARKER=1
SERVER_MARKER=2
VALID_MOVES=("0","1","2")
clients=[]


def start_server(host_ip, port_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    with server_socket:
        print("Server started!")
        print(HOST)
        server_socket.bind((host_ip, port_addr))
        while True:
            print("\nWaiting for client connections...")
            server_socket.listen()
            client_conn, client_addr = server_socket.accept()
            print(f"Client connected at {client_addr}")
            clients.append(client_conn)
            if len(clients) == 2:
                handle_clients()
            #handle_client(client_conn, client_addr)


def handle_clients():
    client_one = clients[0]
    client_two = clients[1]
    while True:

        client_one.send(bytes("send", "utf-8"))
        client_two.send(bytes("receive", "utf-8"))

        client_one_data = client_one.recv(1024)
        if not client_one_data or client_one_data.decode("utf-8") == EXIT_MESSAGE:
            print("Client 1 ended the connection.\n")
            break
        coordinates_string = client_one_data.decode("utf-8")

        client_two.send(bytes(coordinates_string, "utf-8"))


        client_one.send(bytes("receive", "utf-8"))
        client_two.send(bytes("send", "utf-8"))

        client_two_data = client_two.recv(1024)
        if not client_two_data or client_two_data.decode("utf-8") == EXIT_MESSAGE:
            print("Client 2 ended the connection.\n")
            break
        coordinates_string = client_two_data.decode("utf-8")

        client_one.send(bytes(coordinates_string, "utf-8"))


if __name__ == "__main__":
    start_server(host_ip=HOST, port_addr=PORT)