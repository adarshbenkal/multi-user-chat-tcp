import socket 
import threading 
HOST='127.0.0.1'
PORT=9000


def handle_client(client_socket,address):
    print(f"client connected{address}")
    while True:
        data=client_socket.recv(1024)
        if not data:
            break
        print(f"{address}:{data.decode()}")
    print(f"client disconnected:{address}")
    client_socket.close()

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()

print(f"server listening on {HOST}:{PORT}")
while True:
    client_socket,address=server_socket.accept()
    thread=threading.Thread(
        target=handle_client,
        args=(client_socket,address)
    )
    thread.start()