import socket
from threading import Thread

host = socket.gethostbyname(socket.gethostname())  # Host Ip
port = 756

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
            msg = client.recive(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(index)
            nickname = nicks[index]
            nicks.remove(nicks[index])
            broadcast(f"{nickname} left the chat".encode('utf-8'))
            stop = True


def main():
    print('The server is running...')
    while True:
        client, addr = server.accept()  # The code about going to be only exec a when user connect
        print(f'Connected to {addr}')
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicks.append(nickname)
        clients.append(client)
        print(f'nk_name is {nickname}')
        broadcast(f'{nickname} has joined the chat'.encode('utf-8'))
        client.send(f'You are now connected'.encode('utf-8'))
        thread = Thread(target=handle_connection, args=(client,))
        thread.start()


main()
