import socket
from tic_tac_toe import TicTacToe


PORT=9999
EXIT_MESSAGE="goodbye"
CLIENT_MARKER=1
SERVER_MARKER=2
VALID_MOVES=("0","1","2")


def start_client(host_ip, port_addr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with client_socket:
        client_socket.connect((host_ip, port_addr))

        board = TicTacToe()
        print(board)

        while True:
            valid_input = False
            while not valid_input:
                row = input("Enter row: ")
                col = input("Enter col: ")
                if row in VALID_MOVES and col in VALID_MOVES:
                    valid_input = True
                else:
                    print("Please enter valid row and column:", VALID_MOVES)
            board.place(int(row), int(col), CLIENT_MARKER)
            print(board)

            client_socket.send(bytes(row+col, "utf-8"))
            if board.is_winner():
                print("You won!")
                break
            if board.is_draw():
                print("Draw!")
                break

            print("Waiting for server coordinates..")
            incoming_data = client_socket.recv(1024)
            if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
                print(f"Server connection closed.")
                break
            coords_string = incoming_data.decode("utf-8")
            client_row = int(coords_string[0])
            client_col = int(coords_string[1])
            board.place(client_row, client_col, SERVER_MARKER)
            print(board)
            if board.is_winner():
                print("Client won!")
                break
            if board.is_draw():
                print("Draw!")
                break
        print("Connection has closed.")




if __name__=="__main__":
    host_ip = input("Enter the host ip address: ")
    start_client(host_ip=host_ip, port_addr=PORT) 
