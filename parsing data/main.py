from time import time
import pickle
from platform import node, python_version_tuple

'''
The process of converting the data back into its component parts is known as parsing.
The current_time variable is a float, so will need converting to a string before adding to the message:

current_time = str(current_time) message = current_time So that each data item can be separated from the next, 
a special character can be added between the variables. Commas are often used to separate data items, so add a comma 
to the end of the message, too: 

message = message + "," The network_name variable is a string, so it can be added to the message with an additional 
comma to separate it from the rest of the message: 

message = message + network_name + ","
The python_version variable is a tuple of three string values for the major, minor, and revision numbers; for example, 3.7.3 would be ('3', '7', '3'). Each value can be split out, separated by a comma, and added to the message:

message = message + python_version[0] + "," + python_version[1] + "," + python_version[2]
This would construct a message with this structure:

current time,network name,major,minor,revision

For example:

123456.7890,my computer,3,7,3
Finally, the message needs to be encoded into bytes before it can be sent:

data = message.encode()

The data can then be sent and parsed (or reconstructed) by the server into the three separate variables when it is received.

The following code would decode the bytes received by the server and parse the message into the original data:

message = data.decode()
parts = message.split(",")
current_time = float(parts[0])
network_name = parts[1]
python_version = (parts[2], parts[3], parts[4])
Even for a relatively simple message, the code required to parse it is getting complicated. It would be relatively slow to run, difficult to change, and susceptible to errors.


'''

current_time = time()
network_name = node()
python_version = python_version_tuple()

message = (current_time, network_name, python_version)  # creates the tuple of the time, network name and python version
data = pickle.dumps(message)

print(data)

# python has a library called pickle that can convert variables, lists, objects, or just about anything into bytes
# and back again.

'''
Data is a string of bytes right now, but you can deserialize it again by using the pickle loads function\
This means you can call the original variables from the tuple
'''

message1 = pickle.loads(data)

print(message1)

current_time = message1[0]
network_name = message1[1]
python_version = message1[2]
