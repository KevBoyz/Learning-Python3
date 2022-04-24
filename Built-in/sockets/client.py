import socket

host = socket.gethostbyname(socket.gethostname())
port = 7562

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))  # Request the server to connect
    s.sendall(bytes('Ola!', 'utf-8'))
    data = s.recv(1024)

print('Received: ', repr(data))
