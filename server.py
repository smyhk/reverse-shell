import socket

host = '127.0.0.1'
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    print('Listening on port:', port)

    # returns a new socket object representing the connection and a tuple holding the address of the client
    conn, addr = sock.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
