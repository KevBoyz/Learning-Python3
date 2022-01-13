import socket
from threading import Thread

host = socket.gethostbyname(socket.gethostname())  # Host Ip
port = 7562

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Net, tcp sockets
server.bind((host, port))

server.listen()

clients = []
nicks = []


def broadcast(msg):
    for client in clients:
        client.send(msg)


def handle_connection(client):
    stop = False
    while not stop:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            try:
                index = clients.index(client)
                clients.remove(index)
                nickname = nicks[index]
                broadcast(f"{nickname} left the chat".encode('utf-8'))
                nicks.remove(nicks[index])
                stop = True
            except ValueError:
                nick = nicks[clients.index(client)]
                print(f'Value error: User {nick} force a disconnection')
                stop = True


def main():
    print(f'The server is running... Host: {host} Port: {port}')
    while True:
        client, addr = server.accept()  # The code about going to be only exec a when user connect
        print(f'Device connected: {addr}', end=" ")
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicks.append(nickname)
        clients.append(client)
        print(f'Nickname: {nickname}')
        broadcast(f'{nickname} has joined the chat'.encode('utf-8'))
        client.send(f''.encode('utf-8'))
        thread = Thread(target=handle_connection, args=(client,))
        thread.start()


main()
