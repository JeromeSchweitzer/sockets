import socket
from tic_tac_toe import TicTacToe


HOST=socket.gethostbyname(socket.gethostname())
PORT=9999
EXIT_MESSAGE="goodbye"
CLIENT_MARKER=1
SERVER_MARKER=2
VALID_MOVES=("0","1","2")
CLIENTS=[]


def start_server(host_ip, port_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    with server_socket:
        print("Server started")
        print(HOST)
        server_socket.bind((host_ip, port_addr))

        while True:
            print("Listening for clients...")
            server_socket.listen()
            client_conn, client_addr = server_socket.accept()
            #handle_client(client_conn, client_addr)
            CLIENTS.append(client_conn)
            if len(CLIENTS) == 2:
                handle_clients()


def handle_client():
    client_one = CLIENTS[0]
    client_two = CLIENTS[1]

    while True:
        client_one.send(bytes("send", "utf-8"))
        client_two.send(bytes("receive" "utf-8"))

        client_one_data = client_one.recv(1024)
        if not client_one_data or client_one_data.decode("utf-8") == EXIT_MESSAGE:
            print("Client 1 ended the connection.")
            break
        client_two.send(client_one_data)


        client_one.send(bytes("receive", "utf-8"))
        client_two.send(bytes("send" "utf-8"))

        client_two_data = client_two.recv(1024)
        if not client_two_data or client_two_data.decode("utf-8") == EXIT_MESSAGE:
            print("Client 2 ended the connection.")
            break
        client_one.send(client_two_data)



if __name__=="__main__":
   start_server(host_ip=HOST, port_addr=PORT) 


