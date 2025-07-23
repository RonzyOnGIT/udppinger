# client will send 10 pings to a server and server will return capitalized message and compute the RTT (time it takes for ping to reach server and pong to reach client)
from socket import *
import time

serverName = input("Enter server IP: ")
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# socket will wait up to 1 second before declaring packet as lost
clientSocket.settimeout(1)

count = 0

while count < 10:
    message = input("Enter message for server: ")

    try:
        # send udp packet to server
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        packetSentTime = int(round(time.time() * 1000))

        # receive response from server
        response, serverAddress = clientSocket.recvfrom(1024)

        packetArriveTime = int(round(time.time() * 1000))

        # RTT
        ping = packetArriveTime - packetSentTime

        count += 1

        print("Ping #" + str(count) + " " + str(ping))
        print("message: " + response.decode() + "\n")
    except timeout:
        count += 1
        print("Ping #" + str(count) + " " + "packet lost\n")

clientSocket.close()






