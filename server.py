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





'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        b = TicTacToe()
        while not b.check_win() and np.nan not in b.board:
            data = conn.recv(1024)
            if not data:
                pass
            conn.send(data)
'''

'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname('localhost'), 1234))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address}")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
'''
