import threading
import socket
host_ip = "127.0.0.1"
port = 4444
name = input("Enter Name: ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host_ip,port))
def client_receive():
    while True:
        try:
            msg_received = client.recv(1024).decode()
            if msg_received == "Name ?":
                client.send(name.encode())
            else:
                print(msg_received)
        except:
            print("Some Error Occurred!")
            client.close()
            break
def client_send():
    while True:
        msg = f'{name}: {input("")}'
        client.send(msg.encode())
thread_receiver = threading.Thread(target=client_receive)
thread_receiver.start()
thread_sender = threading.Thread(target=client_send)
thread_sender.start()
