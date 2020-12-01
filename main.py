import socket

HOST = "192.168.0.8"
PORT = 12500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected to ", addr)
        while True:
            print("Waiting on data...")
            data = conn.recv(1024)
            print(data)
            print("Text to send: ",end="")
            conn.sendall(bytes(input(),"UTF8"))