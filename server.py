import socket
import threading


HOST=socket.gethostbyname(socket.gethostname())
PORT=9999
EXIT_MESSAGE="goodbye"
CLIENTS={}


def send_to_all(incoming_data, sending_addr):
    for addr in CLIENTS:
        #print(addr)
        #print(conn)
        if addr != sending_addr:
            CLIENTS[addr].send(incoming_data)


def receive_data(client_conn, client_addr):
    while True:
        incoming_data = client_conn.recv(1024)
        if not incoming_data or incoming_data.decode("utf-8") == EXIT_MESSAGE:
            print("Client ended the connection.")
            CLIENTS.pop(client_addr)
            break
        send_to_all(incoming_data, sending_addr=client_addr)


def start_server(host_ip, port_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(HOST)

    with server_socket:
        server_socket.bind((host_ip, port_addr))
        while True:
            server_socket.listen()
            client_conn, client_addr = server_socket.accept()
            CLIENTS[client_addr] = client_conn
            client_thread = threading.Thread(target=receive_data, args=(client_conn, client_addr))
            client_thread.start()


if __name__ == "__main__":
    start_server(host_ip=HOST, port_addr=PORT)

