import socket


HOST="127.0.0.1"
PORT=8888
EXIT_MESSAGE="goodbye"


def start_server(host_ip, port_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with server_socket:
        server_socket.bind((host_ip, port_addr))
        while True:
            server_socket.listen()
            client_conn, client_addr = server_socket.accept()
            handle_client(client_conn, client_addr)


def handle_client(client_conn, client_addr):
    print(f"Connected by {client_addr}")

    with client_conn:
        while True:
            incoming_data = client_conn.recv(1024)
            if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
                print("Client ended the connection.")
                break

            print("Received: \"%s\"" % incoming_data.decode("utf-8"))

            outgoing_msg = input("Send to client: ")
            outgoing_data = bytes(outgoing_msg, "utf-8")
            client_conn.send(outgoing_data)
            if outgoing_msg == EXIT_MESSAGE:
                print("You ended the connection.\n")
                break


if __name__ == "__main__":
    start_server(host_ip=HOST, port_addr=PORT)

