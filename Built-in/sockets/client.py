import socket

host = socket.gethostbyname(socket.gethostname())
port = 7562


# s.connect_ex  # Connect without stop te application

"""
import socket

host = socket.gethostbyname(socket.gethostname())
port = 7562

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))  # Request the server to connect
    s.sendall(b'Ola!')
    data = s.recv(1024)

print('Recebido: ', repr(data))
"""
