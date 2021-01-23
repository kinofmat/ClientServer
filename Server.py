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

# The socket is created and the server is being hosted at the specified IP address and port.
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 56744))
# Look for a connection from the client. 
serv.listen(5)

# Enter a loop for as long as the server is open. . . or an infinte loop. 
while True:
    # Store where the incoming connection is coming from.
    conn, addr = serv.accept()
    # Notify where this connection is coming from.
    print("Connected to ", addr)
    from_client = ''
    counter = 0

    # While there is a connection with the client allow for data to be transmitted.
    while True:
        # Establish the connection and packet size. 
        data = conn.recv(4096)
        # When there is no longer a connection exit.
        if not data: break

        """
        This if structure test for the three different circumstances I allowed in the code.
        First is the text sent back and forth when the connection is first established.
        The second is when the client wants a file.
        The last is when the client is sending a file. 
        """
        if data.decode() == "I am the Client":
            from_client += data.decode()
            print (from_client)
            conn.send("I am the Server".encode())
        elif data.decode() == "Request file":
            # Let the server know what is going on
            print("Your Client has requested a file.")
            # Get the folder path
            fullfile = get_file()
            
            # Check that the path exists. If it does not prompt for input again.
            try:
                filed = open(fullfile, "rb")
            except:
                print("\nError! File not found.\nPlease check your spelling, the directory path, or that the file exists\n")
                fullfile = get_file()
                filed = open(fullfile, "rb")

            # Create a loop to send through all of the information in the file. Once this is done close the file and exit the greater while loop.
            for text in filed:
                conn.send(text)
            filed.close()
            break
        
        else:
            # Make sure to get the file path
            if counter == 0:
                place = send_file()
            # Open the file in binary to receive, then write it, then close it. 
            filer = open(place, "ab")
            filer.write(data)
            filer.close()
            counter += 1

    # Close the connection and print a display message to let the user know what is happening. 
    conn.close()
    print ('Client disconnected')