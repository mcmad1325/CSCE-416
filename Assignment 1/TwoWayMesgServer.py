import socket
import sys

if len(sys.argv) != 3:
    print("Please type in the terminal: python TwoWayMesgServer.py <portNumber> <serverName>")
    sys.exit(1)

port = int(sys.argv[1])
server_name = sys.argv[2]

print(f"Waiting for a client...")

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(('', port))
    server_socket.listen(1)

    # Accept a client connection
    conn, client_addr = server_socket.accept()
    print(f"Connected to client at {client_addr}")

    try:
        while True:
            client_message = conn.recv(1024).decode()
            if not client_message:
                print("Client disconnected.")
                break
            print(f"Client: {client_message}")

            server_message = input("Server> ")
            conn.sendall(f"{server_name}: {server_message}".encode())

    except Exception as e:
        print(f"Error during communication: {e}")
    finally:
        conn.close()

except Exception as e:
    print(f"Server initialization error: {e}")
finally:
    server_socket.close()
    print("Server socket closed.")
