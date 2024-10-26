import socket

HOST='192.168.0.42'
PORT=65432

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    msg=input('Enter a message (exit to quit): ')
    if msg.lower() == 'exit':
        client_socket.sendall(msg.encode())
        break
    client_socket.sendall(msg.encode())
    data=client_socket.recv(1024)
    print('Received: ',data.decode())
client_socket.close()
print('Connection closed')