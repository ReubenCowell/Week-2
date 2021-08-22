# The client UDP socket code
import socket  # imports the socket module

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = input("What Ip address ")
port_number = int(input("What port would you like to connect to?"))
#  client does not need to bind!!!
address = (ip_address, port_number)

udp_client.sendto("Hi there".encode(), address)
print("connected to server")
