import socket
import selectors
import types

host = socket.gethostbyname(socket.gethostname())
port = 7562
sel = selectors.DefaultSelector()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)  # Multiprocess of accepts
s.bind((host, port))
print(f'The server is running... Host: {host} Port: {port}')
s.listen()
sel.register(s, selectors.EVENT_READ, data=None)


def accept_warpper():
    conn, addr = s.accept()
    conn.setblocking(False)  # exec and not stop application


try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                ...
except:
    pass



"""
import socket

host = socket.gethostbyname(socket.gethostname())
port = 7562  # > 1024

# Params: Net type, Conn type; Physical net, Socket stream -> can be archive block
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))  # Up server to port
    print(f'The server is running... Host: {host} Port: {port}')
    s.listen()  # Wait a client...
    conn, addr = s.accept()  # Client has arrived! Accept he? (no args = yes for all)
    with conn:  # Receive all client bytes and exit
        print(f'Client data: {addr}')
        while True:
            data = conn.recv(1024)  # Max of bytes to receive per package
            if not data:
                break
            conn.sendall(data)  # Send all bytes back to client in one package
"""
