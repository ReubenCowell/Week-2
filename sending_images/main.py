from PIL import Image
import pickle
import socket
import time
from random import randint 
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # the sets up as a client

# gets the image to send:
image = Image.open("/Users/reubencowell/OneDrive - Joyce Frankland Academy/Coding/Python/Networking with python/Week-2/sending_images/image.bmp")

width, height = image.size  # gets the height of the image
print(width, height)  # displays it to the user
tot_pixels = width*height
udp_client.sendto(str(tot_pixels).encode(), ("127.0.0.1", 20001))
print(tot_pixels)

# for every row, send every pixel's x and y coordinates to the server
for y in range(height):
    for x in range(width):
        pos = (x, y)
        rgba = image.getpixel(pos)  # gets the pixel and sees its
        message = (pos,rgba)
        data = pickle.dumps(message)
        udp_client.sendto(data, ("127.0.0.1", 20001))  # sends the data (the position and rgba value)
        time.sleep(0.001)
print('sent image')  
