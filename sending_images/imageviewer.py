import socket
import pickle
from fl_networking_tools import ImageViewer

viewer = ImageViewer()


def get_pixel_data():
    while True:
        data, client_address = udp_server.recvfrom(1024)
        message = pickle.loads(data)
        pos = message[0]
        rgba = message[1]
        viewer.put_pixel(pos, rgba)
        print(pos,rgba)


udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 20001))

viewer.start(get_pixel_data)
