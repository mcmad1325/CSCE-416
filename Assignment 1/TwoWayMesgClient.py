import socket
import sys

if len(sys.argv) != 4:
    print("Please type this in the terminal: python TwoWayMesgClient.py <serverAddress> <portNumber> <clientName>")
    sys.exit(1)

server_address = sys.argv[1]
port = int(sys.argv[2])
client_name = sys.argv[3]

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, port))

print(f"Client> Connected to server at ('{server_address}', '{port}')")

try:
    while True:
        try:
            # Send a message to the server
            client_message = input("Client> ")
            client_socket.sendall(f"{client_name}: {client_message}".encode())
        except EOFError:
            print("\nClient> Disconnected.")
            break

        # Receive a message from the server
        server_message = client_socket.recv(1024).decode()
        if not server_message:
            print("Client> Server disconnected.")
            break
        print(f"Client> {server_message}")

finally:
    client_socket.close()
