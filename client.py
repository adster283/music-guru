import random
import socket
import sys

# creating a socket object
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

# default port for socket
port = input("Please enter the port number you want to connect to: ")

# setting up the server address
try:
    address = input("Please enter the address you want to connect to: ")
    host_ip = socket.gethostbyname(str(address))
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, int(port)))

# receive data range from the server
data = s.recv(1024)  # Setting the buffer size as 1024
print("Server Response:", data.decode())


# send the selected year to the server
# send random year if not in valid range
range = data.decode().split(", ")
year = input("Please enter a year between " +
             range[0] + " and " + range[1] + ": ")

if (int(year) >= int(range[0]) and int(year) <= int(range[1])):
    s.send(year.encode())
else:
    year = random.randint(int(range[0]), int(range[1]))
    print("Specified year out of range (1950-2009), using random date instead :", year)
    s.send(str(year).encode())

# s.send("1950".encode())

# receive the song from the server
data = s.recv(1024)  # Setting the buffer size as 1024
print("Server Response:", data.decode())

print("Connection closed.")
