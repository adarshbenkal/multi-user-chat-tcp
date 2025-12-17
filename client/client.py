import socket
import threading

HOST = "127.0.0.1"
PORT = 9000


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if message:
                print(message.decode())
        except:
            break


def start_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    thread.start()

    while True:
        msg = input()
        sock.sendall(msg.encode())


if __name__ == "__main__":
    start_client()
