import socket
import threading
from time import sleep
from random import choice

from tic_tac_toe import TicTacToe


HOST=socket.gethostbyname(socket.gethostname())
PORT=9999
EXIT_MESSAGE="goodbye"
CLIENT_MARKER=1
SERVER_MARKER=2
VALID_MOVES=("0","1","2")


def start_server(host_ip, port_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    with server_socket:
        print("Server started")
        print(HOST)
        server_socket.bind((host_ip, port_addr))

        while True:
            server_socket.listen()
            client_conn, client_addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_conn, client_addr))
            client_thread.start()
            #handle_client(client_conn, client_addr)


def handle_client(client_conn, client_addr):
    print(f"Connected by client {client_addr}")

    with client_conn:
        board = TicTacToe()
        while True:
            incoming_data = client_conn.recv(1024)
            if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
                break
            coords_string = incoming_data.decode("utf-8")
            client_row = int(coords_string[0])
            client_col = int(coords_string[1])
            board.place(client_row, client_col, CLIENT_MARKER)
            if board.is_winner():
                print(f"You lost the game with {client_addr}")
                break
            if board.is_draw():
                print(f"Game with {client_addr} drawn")
                break

            sleep(2)
            valid_move = False
            while not valid_move:   # The best AI is here
                row = choice(VALID_MOVES)
                col = choice(VALID_MOVES)
                valid_move = board.place(int(row), int(col), SERVER_MARKER)

            client_conn.send(bytes(row+col, "utf-8"))
            if board.is_winner():
                print(f"You won the game with {client_addr}")
                break
            if board.is_draw():
                print(f"Game with {client_addr} drawn")
                break
    print(f"Connection with {client_addr} terminated")



if __name__=="__main__":
   start_server(host_ip=HOST, port_addr=PORT) 


