import socket
import threading

HOST = "127.0.0.1"
PORT = 9000

clients = []
lock = threading.Lock()


def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.sendall(message)
                except:
                    clients.remove(client)


def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address}")

    with lock:
        clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
    finally:
        print(f"[DISCONNECTED] {address}")
        with lock:
            clients.remove(client_socket)
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address),
            daemon=True
        )
        thread.start()


if __name__ == "__main__":
    start_server()
