import socket
from threading import Thread

IP_ADRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096

clients = ()

def setup():
    global PORT
    global IP_ADRESS
    global SERVER

    print("\t\t\t\t\t Music Sharing App")

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADRESS, PORT))

    SERVER.listen(100)

    print("\n\t\t\t\tServer is waiting for incoming connections...\n")

    acceptConnections()


setup_thread = Thread(target = setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()

        #print(client.addr)