import socket
import os
HOST='192.168.0.42'
PORT=65432

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

def sendfile(filepath):
    filename=os.path.basename(filepath)
    s.sendall(filename.encode())
    with open(filepath,"rb") as f:
        while True:
            data=f.read(1024)
            if not data:
                break
            s.sendall(data)
    print(f'Sent: {filename}')
path=input("Enter the Absolute path of the file")
sendfile(path)