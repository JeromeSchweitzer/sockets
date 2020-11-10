import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()
conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data:
        print("client disconnected")
        break
    print("received", repr(data))




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
