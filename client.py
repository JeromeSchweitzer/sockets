import socket

HOST = '127.0.0.1'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    outgoing_msg = input("enter input: ")
    client_socket.send(bytes(outgoing_msg, "utf-8"))
    if outgoing_msg == "goodbye":
        break
