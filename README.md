# Overview

In this code I was testing my ability to read through sample code and pushed the limits of my understanding of how to work with python. I used a new python library that I had no exposure to before and read the HOWTO to gain an understanding of how to use it.  

I created a simple client and server that can pass files to each other. Start the Server code first, and then the client code. The client will prompt you if you would like to send or recieve a file. The server portion of the code will stay open until you stop the program. This will allow for multiple clients to connect, or the same one if an error happens. 

I had never done anything relating to the creation of a network before and wanted to try it out and learn more about it. All that this can do for now is send a single file.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Network Demo Video](https://youtu.be/Oi9ErC7f-mc)

# Network Communication

This is a client/server but could be adapted to a peer-to-peer. 

The sockets use TCP, and for this software the port 56744 is used, since it is a higher socket it is less likely that another program may be using it. 

The messages are encoded in binary, before being sent through the socket layer. For the files they are opened already in binary, while some of the messages in string that are sent back and forth are first encoded, and then decoded. The server can only accept simple txt formats, while the client can accept many types. 

# Development Environment

I used Python, Visual Studio Code, and Git. For creating this software. I also used the socket library to create the well sockets for the network.

# Useful Websites

* [Python Docs - HOWTO](https://docs.python.org/3.6/howto/sockets.html#sockets)
* [Python Docs - Socket](https://docs.python.org/3.6/library/socket.html)
* [PubNub - tutorial on creating network](https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/)

# Future Work

* Add functionality to automatically send the file name, along with the file. This would remove any confusion over what type of extention the file would be, and streamline it for the user.
* Add functionality to allow for multiple files to be sent.
* Adjust the size to allow for larger files to be sent as well. 
* Ajust to allow the server to recieve multiple types of files. 