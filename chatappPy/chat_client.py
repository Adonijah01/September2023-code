import socket
import threading

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server host and port
host = '127.0.0.1'
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Function to receive messages from the server
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            # An error occurred, likely the server closed the connection
            print("Connection closed.")
            break

# Create threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

# Start the threads
send_thread.start()
receive_thread.start()

