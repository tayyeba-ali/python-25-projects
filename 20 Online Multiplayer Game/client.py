import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(("127.0.0.1", 5555))
except:
    print("❌ Cannot connect to the server.")
    exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024)
            if not message:
                print("❌ Server disconnected.")
                break
            print(message.decode())
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    try:
        message = input()
        if message.lower() == "exit":
            client.send(message.encode())
            client.close()
            break
        client.send(message.encode())
    except:
        print("❌ Lost connection to server.")
        break
