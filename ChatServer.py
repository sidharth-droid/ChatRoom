import socket
import threading
host_IP = "127.0.0.1"
port = 4444

serverObj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverObj.bind((host_IP,port))
serverObj.listen()

clients_list = []
clients_name = []

def broadcast_message(msg):
    for client in clients_list:
        client.send(msg)
def client_handler(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast_message(msg)
        except:
            client_index = clients_list.index(client)
            client_name = clients_name[client_index]
            clients_list.remove(client)
            client.close()
            broadcast_message(f'{client_name} has left the chat room'.encode())
            clients_name.remove(client_name)
            break
def receive_connections():
    while(True):
        print("Server Running...")
        client,addr = serverObj.accept()
        print(f"Connection established with client {str(addr)}")
        client.send("Name ?".encode())
        client_name = client.recv(1024).decode()
        clients_name.append(client_name)
        clients_list.append(client)
        print(f"Client Name is {client_name}")
        broadcast_message(f"{client_name} is connected to chat room".encode())
        client.send("\nYou Are connected to the room ".encode())
        thread = threading.Thread(target=client_handler,args=(client,))
        thread.start()

receive_connections()

