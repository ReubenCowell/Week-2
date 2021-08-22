# UDP Server from the course
import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 2001))

data, client_address = udp_server.recvfrom(1024)
# data = 'hi there'
# udp_server.sendto(data, client_address)
print("client connected")

data, client_address = udp_server.recvfrom(1024)
