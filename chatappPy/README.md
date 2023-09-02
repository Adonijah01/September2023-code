Basic Python Chat Application

This is a basic chat application implemented in Python using sockets. It consists of a simple server and client that can send messages back and forth. Please note that this is a minimalistic example and should not be used for production purposes.
Features

    Simple server-client architecture for sending messages.
    Multiple clients can connect to the server and chat simultaneously.
    Messages are broadcasted to all connected clients.

Prerequisites

    Python 3.x installed on your computer.

Getting Started
Running the Server

    Open a terminal or command prompt.

    Navigate to the directory containing chat_server.py.

    Run the server script by executing the following command:

    bash

    python chat_server.py

    The server will start and listen for incoming connections on 127.0.0.1:12345 by default.

Running the Client(s)

    Open one or more additional terminal/command prompt windows, depending on how many clients you want to simulate.

    Navigate to the directory containing chat_client.py in each terminal.

    Run the client script in each terminal by executing the following command:

    bash

    python chat_client.py

    Each client will connect to the server running on 127.0.0.1:12345 by default. You can run multiple client terminals to simulate multiple users.

How to Use

    In the client terminals, type your messages and press Enter to send them.
    Messages you send will be received by all connected clients, including your own.
    Simulate a multi-user chat by running multiple client terminals and sending messages between them.

Exit

    To exit the server and clients, press Ctrl+C in each terminal to stop the scripts.

Note

This is a basic chat application intended for educational purposes. In a real-world application, you would need to handle various error cases, add more features, and ensure security for a robust chat application. Use this as a starting point for more advanced projects.
License

This project is licensed under the MIT License - see the LICENSE file for details.
