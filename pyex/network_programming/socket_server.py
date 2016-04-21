from socket import *

host = ''
port = 2001

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
while True:
    conxn, address = sock.accept()
    print('Server is connected by ', address)
    while not False:
        data = conxn.recv(4112)
        if not data:
            break
        conxn.send(b'this is an echo of the client originating data: ' + data)
    conxn.close()
