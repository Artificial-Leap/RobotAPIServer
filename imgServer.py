import threading
import cv2
import socket
import pickle

running = True
client = None

def on_new_client(clientsocket,addr):
    global client, running
    client = clientsocket

    print("Connected to: " + str(addr))
    while running:
        x = clientsocket.recvfrom(1000000)
        clientip = x[1][0]
        data = x[0]

        data = pickle.loads(data)

        img = cv2.imdecode(data, cv2.IMREAD_COLOR)
        
        cv2.imshow('Img Server', img)
        
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    clientsocket.close()

def closeClient():
    global running, client
    running = False

def send(msg):
    global client
    client.send(msg)

def initImgServer():
    s = socket.socket()
    ip = "127.0.0.1"
    port = 7777
    s.bind((ip, port))
    s.listen(1)
    print("listening")

    while True:
        c, addr = s.accept()   
        threading.Thread(target=on_new_client, args=(c,addr)).start()
        
    s.close()