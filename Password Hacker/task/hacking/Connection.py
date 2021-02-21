import json
import socket


def connect(address):
    client_socket = socket.socket()
    client_socket.connect(address)
    return client_socket
