# Socket is the library necessary to run this connection.
import socket

"""
get_file doesn't need any arguments. It will prompt the user for input of where the file to be sent is located. 
Then it will ask for which file and create a path for it. It returns this file path.
"""
def get_file():
    filepath = input("What is the file path you wish to select a file from? ")
    filename = input("What is the name of the file you want to obtain? (include the extention) ")
    fullfile = filepath + "/" + filename
    return fullfile

"""
send_file does not require any arguments either. It will ask for the folder to save the file in.
Then it will ask what you want to save the file as. It will return the file path from this information.
"""
def send_file():
    filepath = input("Where would you like to place this file? (Please provide folder path) ")
    filename = input("What would you like to name this file? ")
    fullfile = filepath + "/" + filename
    return fullfile

# The socket is created, and the client connects to the server at the specified IP address, and port.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 56744))
# A short message is passed back and forth to show that the connection was established. 
client.send("I am the Client".encode())
# Create the data stream with a specified amount of bites that can be sent.
from_server = client.recv(4096)
print (from_server.decode())

"""There is a short print statement to determine what the user would like to do.
From there is goes into a if statement to either send a file or receive one."""
filler = input("If you would like to request a file type R.\nIf you would like to send a file type S. ")
if filler.upper() == "R":
    # Tell the server we want a file
    client.send("Request file".encode())
    counter = 0
    # Go into a loop so that we can receive the full file. 
    while True:
        from_server = client.recv(4096)
        # Exit the loop if there is no longer a connection.
        if not from_server: break
        # When it is the first time through the loop we need to get the location to save the file at.
        if counter == 0:
            place = send_file()
        """
        The data is passed as binary, so the file needs to be opened in a binary reading mode.
        Add the code to the file, and then keep the code clean by closing the file before the end of the loop.
        """
        filer = open(place, "ab")
        filer.write(from_server)
        filer.close()
        counter += 1
elif filler.upper() == "S":
    # Make sure we get the location of what file we will be sending
    fullfile = get_file()
    # Check that it is a valid file location
    try:
        filed = open(fullfile, "rb")
    # If not try entering in the path again.
    except:
        print("\nError! File not found.\nPlease check your spelling, the directory path, or that the file exists\n")
        fullfile = get_file()
        filed = open(fullfile, "rb")

    # A loop to send the file information across to the server, and then close the file after exiting the loop.
    for text in filed:
        client.send(text)
    filed.close()
else:
    print("Error!")

# Just like closing a file the connection needs to be closed too. 
client.close()