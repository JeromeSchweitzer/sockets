import socket
import threading


#HOST="127.0.0.1"
PORT=9999
EXIT_MESSAGE="goodbye"


def send_data(client_socket):
    while True:
        outgoing_msg = input("Enter message: ")
        outgoing_data = bytes(outgoing_msg, "utf-8")
        client_socket.send(outgoing_data)
        if outgoing_msg == EXIT_MESSAGE:
            print("You ended the connection.")
            break


def receive_data(client_socket):
    while True:
        incoming_data = client_socket.recv(1024)
        if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
            print("Server ended the connection.\n")
            break
        print("\nReceived: \"%s\"Enter message: " % incoming_data.decode("utf-8"))


def start_client(host_ip, port_addr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_ip, port_addr))

    receive_thread = threading.Thread(target=receive_data, args=(client_socket,))

    receive_thread.start()
    send_data(client_socket)


if __name__ == "__main__":
    host = input("Enter host ip: ")
    start_client(host_ip=host, port_addr=PORT)
