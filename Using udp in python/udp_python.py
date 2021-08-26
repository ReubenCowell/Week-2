# The client UDP socket code
import socket  # imports the socket module


def reply():  # this is the main body of how the the reading and replying works
    data, client_address = usr_socket.recvfrom(1024)
    # the formatting for the received messages
    print('Message received: \n--------------------------- \n{}\n---------------------------'.format(data.decode()))
    msg = input('What is your reply?').encode()  # gets the reply to send and encodes it
    usr_socket.sendto(msg, client_address)  # sends the reply


user = input('Would you like to be the server (1) or the client(2)')
if user == '1':  # the server user
    ip_address = "0.0.0.0"  # sets up the ip address
    port_num = 2001  # sets up the port
    listening_socket = (ip_address, port_num)
    usr_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # sets up the socket with datagram mode
    usr_socket.bind(listening_socket)  # binds the socket to the ip and port
    ip_address, listening_socket = usr_socket.recvfrom(1024)  # receives the initial message
    print(ip_address.decode())  # decodes and prints it to the user
    print("Connection detected at... " + str(ip_address.decode()))  # shows where the connection is from
    usr_socket.sendto("Connected to server".encode(), listening_socket)  # sends an initial message
    print('Waiting for first message....')


elif user == '2':  # the client user
    usr_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # sets up the client socket using datagram
    # gets the IP and PORT that the client will connect to in order to send messages:
    ip_address = input("What Ip address ")
    port_num = int(input("What port would you like to connect to?"))
    #  client does not need to bind!!!
    address = (ip_address, port_num)  # sets uo the address for
    usr_socket.sendto(ip_address.encode(), (ip_address, port_num))  # the initial message to the server

client_address = (ip_address, port_num)
while True:
    reply()
