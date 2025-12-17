import socket
HOST='127.0.0.1'
PORT=9000

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
# socket.AF_INET      # IPv4 addressing
# socket.SOCK_STREAM  # STREAM = TCP


client_socket.connect((HOST,PORT))
while True:
    msg=input("enter a message ")
    client_socket.sendall(msg.encode())
