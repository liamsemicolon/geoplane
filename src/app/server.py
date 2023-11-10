import socket
import pickle  # For deserializing the data

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))  # Replace with your desired IP and port
server.listen()

# Wait for a client to connect
print("Waiting for connection...")
client_socket, address = server.accept()
print(f"Connection from {address}")

# Receive the contadorTiempo variable
data = client_socket.recv(4096)
contadorTiempo = pickle.loads(data)
print(f"Received contadorTiempo: {contadorTiempo}")

# Close the connection
client_socket.close()
server.close()