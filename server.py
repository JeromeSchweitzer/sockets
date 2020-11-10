import socket


def handle_client(client_conn, client_addr):
    print('Connected by', client_addr)
    while True:
        incoming_data = client_conn.recv(1024)
        if not incoming_data:
            client_conn.close()
            print("client disconnected")
            break
        print("received", repr(incoming_data))


HOST = '127.0.0.1'
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

while True:
    server_socket.listen()
    client_conn, client_addr = server_socket.accept()
    handle_client(client_conn, client_addr)

