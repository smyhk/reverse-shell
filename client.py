import socket

host = '127.0.0.1'
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(b'Hello, world')
    data = sock.recv(1024)

print('Received', repr(data))
