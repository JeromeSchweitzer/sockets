import socket
from tic_tac_toe import TicTacToe


#HOST=""
PORT=8888
EXIT_MESSAGE="goodbye"
CLIENT_MARKER=1
SERVER_MARKER=2


def start_client(host_ip, port_addr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with client_socket:
        client_socket.connect((host_ip, port_addr))

        board = TicTacToe()
        print(board)
        while True:
            row = input("Enter row: ")
            col = input("Enter col: ")
            board.place(int(row), int(col), CLIENT_MARKER)
            print(board)

            #coords = row+col
            client_socket.send(bytes(row+col, "utf-8"))
            if board.is_winner():
                print("You won!")
                break

            print("Waiting for server coordinates...")
            incoming_data = client_socket.recv(1024)
            if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
                print("Server ended the connection.\n")
                break
            coordinates_string = incoming_data.decode("utf-8")
            server_row = int(coordinates_string[0])
            server_col = int(coordinates_string[1])
            board.place(server_row, server_col, SERVER_MARKER)
            print(board)
            if board.is_winner():
                print("Server won!")
                break
    print("Connection with server ended.")


if __name__ == "__main__":
    host_ip=input("Enter host IP address: ")
    start_client(host_ip=host_ip, port_addr=PORT)