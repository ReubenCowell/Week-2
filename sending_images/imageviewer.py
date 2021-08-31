import socket
import pickle
from fl_networking_tools import ImageViewer
from random import randint

viewer = ImageViewer()  # starts an imageviewer window


"""
This simple error detection algorithm will work like this:

Receive a pixel.
Store the position of the pixel received.
Receive a new pixel.
Ask whether the position of the new pixel is more than 1 greater in x or y than the last pixel.
If so, a pixel has been lost.
"""

def get_pixel_data():  # gets the pixel data
    while True:
        global lost_pixels
        viewer.text = lost_pixels  # at the top of the image viwer, it will display the number of lost pizels
        data, client_address = udp_server.recvfrom(1024)  
        message = pickle.loads(data)  # 'decrypts the pickle data
        # gets the position and rgba data for each pixel
        pos = message[0]
        rgba = message[1]
        viewer.put_pixel(pos, rgba)  # puts the colour on the imageviewer window
        print(pos,rgba)  # prints the data
        print(last_pixel_updated)  
        if (pos[0] - last_pixel_updated[0] > 1) or (pos[1] - last_pixel_updated[1] > 1): # checks if a pixel is out of sequence by seeing whether their locations subtract to more than one
            lost_pixels += 1  # this is teh variable for the amount of lost pixels
            viewer.text = lost_pixels  # updates the text at the top of the imageviewer window

    #last_pixel_updated = pos

# binds the socket as a datagram server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 20001))

tot_pixels, client_address = udp_server.recvfrom(1024)
print(tot_pixels.decode())

# sets the variables:
lost_pixels = 0     
last_pixel_updated = (-1, -1)
viewer.start(get_pixel_data)  # starts the image viewer with the get_pixel_data function

recvd_pixels = int(tot_pixels.decode()) - lost_pixels
print('Image recieved:\nTotal pixels: {}\nLost pixels: {}\nPixels recieved: {}'.format(tot_pixels,lost_pixels,recvd_pixels))