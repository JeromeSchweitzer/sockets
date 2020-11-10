import socket
from tic_tac_toe import TicTacToe


HOST="127.0.0.1"
PORT=8888
EXIT_MESSAGE="goodbye"
MARKER=1


def start_client(host_ip, port_addr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with client_socket:
        client_socket.connect((host_ip, port_addr))

        board = TicTacToe()
        while not board.is_winner():
            print(board)
            row = input("Enter row: ")
            col = input("Enter col: ")
            board.place(row, col, MARKER)
            print(board)

            client_socket.send(bytes(row+col), "utf-8")
            if board.is_winner():
                break

            incoming_data = client_socket.recv(1024)
            # outgoing_msg = input("Enter message for server: ")
            # outgoing_data = bytes(outgoing_msg, "utf-8")
            # client_socket.send(outgoing_data)
            # if outgoing_msg == EXIT_MESSAGE:
            #     print("You ended the connection.")
            #     break

            # incoming_data = client_socket.recv(1024)
            # if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
            #     print("Server ended the connection.\n")
            #     break
            # print("Received: \"%s\"" % incoming_data.decode("utf-8"))


if __name__ == "__main__":
    start_client(host_ip=HOST, port_addr=PORT)