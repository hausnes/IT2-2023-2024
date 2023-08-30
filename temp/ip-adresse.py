# Import the socket module
import socket

# Ask the user to enter an IP address
ip = input("Enter an IP address: ")

# Try to get the domain name from the IP address
try:
    # Use the gethostbyaddr function to get the domain name
    domain = socket.gethostbyaddr(ip)[0]
    # Print the domain name
    print("The domain name is:", domain)
except:
    # If an error occurs, print a message
    print("Error resolving domain.")