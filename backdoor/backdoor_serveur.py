import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


def socket_receive_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    #print("socket_receive_all_data len : ", data_len)
    while  current_data_len < data_len:
        chunk_len = data_len - current_data_len
        if chunk_len > MAX_DATA_SIZE:
            chunk_len = MAX_DATA_SIZE
        data = socket_p.recv(chunk_len)
        #print("data recues : ", len(data))
        if not data:
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        current_data_len += len(data)
        #print("Total data: ", current_data_len ,"/", data_len)
    return total_data


def socket_send_and_receive_all_data(socket_p,commande):
    if not commande:
        return None
    socket_p.sendall(commande.encode())
    
    header_data = socket_receive_all_data(socket_p, 13)
    longueur_data = int(header_data.decode())
    
    data_recues = socket_receive_all_data(socket_p, longueur_data)
    return data_recues   


s = socket.socket()         # Creation de la socket
s.bind((HOST_IP,HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}")
connection_socket, client_address = s.accept()
print(f"Connexion etablie avec {client_address}")

while True:
    infos_data = socket_send_and_receive_all_data(connection_socket,"infos")
    if not infos_data:
        break
    commande = input(client_address[0] + ":" + str(client_address[1]) + " " + infos_data.decode() + " > ")
    data_recues = socket_send_and_receive_all_data(connection_socket, commande)
    if not data_recues:
        break
    print(data_recues.decode())

s.close()
connection_socket.close()