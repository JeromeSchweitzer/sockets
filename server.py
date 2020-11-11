import socket
from tic_tac_toe import TicTacToe


HOST=socket.gethostbyname(socket.gethostname())
PORT=8888
EXIT_MESSAGE="goodbye"
CLIENT_MARKER=1
SERVER_MARKER=2
VALID_MOVES=("0","1","2")


def start_server(host_ip, port_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    with server_socket:
        print("Server started!")
        print(HOST)
        server_socket.bind((host_ip, port_addr))
        while True:
            print("\nWaiting for client connection...")
            server_socket.listen()
            client_conn, client_addr = server_socket.accept()
            handle_client(client_conn, client_addr)


def handle_client(client_conn, client_addr):
    print(f"Connected by {client_addr}")

    with client_conn:
        board = TicTacToe()
        while True:
            print("Waiting for client coordinates...")
            incoming_data = client_conn.recv(1024)
            if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
                print("Client ended the connection.\n")
                break
            coordinates_string = incoming_data.decode("utf-8")
            client_row = int(coordinates_string[0])
            client_col = int(coordinates_string[1])
            board.place(client_row, client_col, CLIENT_MARKER)
            print(board)
            if board.is_winner():
                print("Client won!")
                break
            if board.is_draw():
                print("Draw!")
                break

            valid_input = False
            while not valid_input:
                row = input("Enter row: ")
                col = input("Enter col: ")
                if row in VALID_MOVES and col in VALID_MOVES:
                    valid_input = True
                else:
                    print("Please enter row and column value of", VALID_MOVES)
            board.place(int(row), int(col), SERVER_MARKER)
            print(board)

            client_conn.send(bytes(row+col, "utf-8"))
            if board.is_winner():
                print("You won!")
                break
            if board.is_draw():
                print("Draw!")
                break


if __name__ == "__main__":
    start_server(host_ip=HOST, port_addr=PORT)