import sys
import socket
import string
import itertools

hostname = sys.argv[1]
port = int(sys.argv[2])
address = (hostname, port)
characters = string.ascii_lowercase + string.digits

def psw():
    for i in range(1000000):
        for password in itertools.product(characters, repeat=(i + 1)):
            password = str("".join(password)).encode()
            yield password


with socket.socket() as my_sock:
    my_sock.connect(address)
    pswd = psw()
    while True:
        message = next(pswd)
        my_sock.send(message)
        response = my_sock.recv(1024).decode()
        if response == "Connection success!":
            print(message.decode())
            break
        elif response == "Wrong password!":
            continue