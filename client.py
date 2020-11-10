import socket

HOST = '127.0.0.1'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        outgoing_msg = input("Enter message for server: ")
        client_socket.send(bytes(outgoing_msg, "utf-8"))
        if outgoing_msg == "goodbye":
            print("You (client) ended connection")
            break

        incoming_data = client_socket.recv(1024)
        if not incoming_data:
            print("Server ended connection")
            break
        print("received", repr(incoming_data))
