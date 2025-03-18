import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("Erreur : impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print("Connecte au serveur")
        break
while True:   
    data_recues = s.recv(MAX_DATA_SIZE)
    if not data_recues:
        break
    print(f"Message: {data_recues.decode()}")
    data_envoye = input("Vous: ")
    s.sendall(data_envoye.encode())
    
s.close()