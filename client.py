
import socket

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    message = input("enter input: ")
    s.send(bytes(message, "utf-8"))
    if message == "goodbye":
        break


'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        outgoing_msg = input("enter message: ")
        s.send(bytes(outgoing_msg, "utf-8"))
        data = s.recv(1024)
        print('Received', repr(data))
'''
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname('localhost'), 1234))

while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
'''
