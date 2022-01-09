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
