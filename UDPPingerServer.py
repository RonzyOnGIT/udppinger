import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # Capitalize the message from the client
    message = message.upper()

    # If rand is less is than 3, we consider the packet lost and do not respond to imitate loss of packets at 20% loss rate
    if rand < 3:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)