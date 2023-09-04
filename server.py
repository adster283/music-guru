import argparse
import socket
import random

"""This function takes a year as a parameter and returns a random top song from that year

PARAMETERS:
year (int): The year to search for

RETURNS:
(str): Random song from the year
"""
def searchSong(year):
    count = 0

    with open('songs.txt', "r") as file:

        for line in file:
            count += 1
            if str(year) in line:
                break

        random_number = random.randint(1, 10)

        for i, line in enumerate(file, start=1):
            if i == count+random_number:
                return (f"In {year} the {random_number+1} song was " + line.strip()[3:])


# Argument parser for port number
parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, help='The port to listen on')
args = parser.parse_args()

# creating a socket object
s = socket.socket()
print("Socket successfully created")

# Checking if port number is valid and assinging it to port if
# it is
if (args.port is None):
    print("No port specified. Please specify a port. Exiting.")
    exit()

port = args.port

# binding the port
try:
    s.bind(('', port))
    print("socket binded to %s" % (port))
except:
    print("Could not bind to port %s" %
          (port) + "The port may be in use. Exiting.")
    exit()

# Listening on port
s.listen(5)
print("socket is listening")

# an infinite loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send the valid range to the client
    c.send('1950, 2009'.encode())
    client_response = c.recv(1024).decode()

    # handle the client response and send the song
    c.send(searchSong(client_response).encode())

    # Close the connection with the client
    c.close()

    # ending the loop 
    break
