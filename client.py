import socket
from time import sleep
import json
import sys


def Main():
    host = '127.0.0.1'
    port = 8888

    mySocket = socket.socket()
    try:
        mySocket.connect((host, port))
    except:
        print('Error, could not connect. Shutting down.')
        sys.exit(0)

    cmd_data = {"type": 1, "body": "this is michael jackson from space"}

    while True:
        message = json.dumps(cmd_data) + '\n'
        try:
            mySocket.send(message.encode())
        except:
            print('Server Error, shutting down.')
            sys.exit(0)

        try:
            response = mySocket.recv(1024).decode()
            print('Received from server: ' + response)
        except:
            print('Server Error, shutting down.')
            sys.exit(0)

        cmd_data['type'] += 1
        sleep(1)

    mySocket.close()


if __name__ == '__main__':
    Main()
