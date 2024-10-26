import socket
import os

HOST = '192.168.0.42'  # The server's hostname or IP address
PORT = 65432           # The port used by the server

def send_file(s, filepath, root_dir):
    relative_path = os.path.relpath(filepath, root_dir)
    s.sendall(f'FILE:{relative_path}'.encode())

    with open(filepath, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data)
    s.sendall(b'EOF')  # Send EOF to indicate end of file transmission
    print(f"Sent file: {filepath}")

def send_folder(s, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            relative_path = os.path.relpath(os.path.join(root, dir), folder_path)
            s.sendall(f'DIR:{relative_path}'.encode())
            print(f"Sent directory: {relative_path}")
        
        for file in files:
            send_file(s, os.path.join(root, file), folder_path)

    s.sendall('END'.encode())

if __name__ == "__main__":
    folder_path = input("Enter absolute path of the folder to send: ")

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
    elif not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory.")
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            send_folder(s, folder_path)
            print(f"Sent folder: {folder_path}")
