import socket

HOST = "107.189.252.102"
PORT = 12500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print("Text to send: ",end="")
    s.send(bytes(input(),"UTF8"))
    print("Waiting on data...")
    data = s.recv(1024)
    while True:
        print(data)
        print("Text to send: ",end="")
        s.send(bytes(input(),"UTF8"))
        print("Waiting on data...")
        data = s.recv(1024)