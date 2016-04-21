from socket import *
import sys

server_host = 'localhost'
server_port = 50006

data = [b'{"coord":{"lon":139,"lat":35},"sys":{"country":"JP","sunrise":1369769524,"sunset":1369821049},"weather":[{"id":804,"main":"clouds","description":"overcast clouds","icon":"04n"}],"main":{"temp":289.5,"humidity":89,"pressure":1013,"temp_min":287.04,"temp_max":292.04},"wind":{"speed":7.31,"deg":187.002},"rain":{"3h":0},"clouds":{"all":92},"dt":1369824698,"id":1851632,"name":"Shuzenji","cod":200}']

if len(sys.argv) > 1:
    server_host = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((server_host, server_port))

for line in data:
    sock.send(line)
    data_received = sock.recv(4112)
    print('The client received: ', data_received)

sock.close()
