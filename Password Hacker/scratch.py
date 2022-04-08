
import sys
import socket
import string
import itertools
import json

hostname = sys.argv[1]
port = int(sys.argv[2])
address = (hostname, port)
characters = string.ascii_lowercase + string.digits

with open('/Users/shlomodahan/Desktop/JetBrains Projects/Password Hacker/passwords.txt', 'r') as file:
    passwords = file.readlines()
passwords = [x.strip() for x in passwords]

possibilities = []
for pswd in passwords:
    possibilities.append(list(map(''.join, itertools.product(*zip(pswd.upper(), pswd.lower())))))

options = []
for list in possibilities:
    for word in list:
        options.append(word)

with socket.socket() as my_sock:
    my_sock.connect(address)
    for pswd in options:
        message = pswd.encode()
        my_sock.send(message)
        response = my_sock.recv(1024).decode()
        if response == "Connection success!":
            print(message.decode())
            break
        elif response == "Wrong password!":
            continue
