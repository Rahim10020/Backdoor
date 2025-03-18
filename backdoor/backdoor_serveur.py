import socket


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


s = socket.socket()         # Creation de la socket
s.bind((HOST_IP,HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}")
connection_socket, client_address = s.accept()
print(f"Connexion etablie avec {client_address}")

while True:
    commande = input("Commande: ")
    connection_socket.sendall(commande.encode())
    data_recues = connection_socket.recv(MAX_DATA_SIZE)
    if not data_recues:
        break
    print(data_recues.decode())

s.close()
connection_socket.close()