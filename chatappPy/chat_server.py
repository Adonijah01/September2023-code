import socket
import threading

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to bind the server to
host = '127.0.0.1'
port = 12345

# Bind the server to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

# List to store client connections
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send message
                clients.remove(client)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            # Remove the client if an error occurs
            clients.remove(client_socket)
            break

# Main server loop
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    # Add the client to the list
    clients.append(client_socket)
    
    # Create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

