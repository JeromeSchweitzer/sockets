import socket


def handle_client(client_conn, client_addr):
    print('Connected by', client_addr)

    with client_conn:
        while True:
            incoming_data = client_conn.recv(1024)
            if not incoming_data:
                print("Client ended connection")
                break
            print("received", incoming_data)
            
            outgoing_msg = input("Enter message for client: ")
            client_conn.send(bytes(outgoing_msg, "utf-8"))
            if outgoing_msg == "goodbye":
                print("You (server) ended connection")
                break


HOST = '127.0.0.1'
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with server_socket:
    server_socket.bind((HOST, PORT))

    while True:
        server_socket.listen()
        client_conn, client_addr = server_socket.accept()
        handle_client(client_conn, client_addr)

