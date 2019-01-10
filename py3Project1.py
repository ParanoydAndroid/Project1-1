# Import socket module
from socket import *
import time


def send_by_byte(output: str, s: socket):
    for i in range(0, len(output)):
        s.send(output[i].encode())
    #s.send('\r\n'.encode())

    return

serverName = '10.12.1.243'
serverPort = 4242

# Create a TCP client socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

to_send = b'\xccWhat is the answer to the Ultimate Question of Life, The Universe, and Everything?'

#send_by_byte(to_send, clientSocket)
clientSocket.send(to_send)

print("Stopping service ...\n")
time.sleep(10)
clientSocket.close()
print("Service stopped!")
