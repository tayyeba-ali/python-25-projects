import socket
import threading
import random

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(5)

print("🎮 Server started — waiting for players...")

players = {}
scores = {}
lock = threading.Lock()
secret_number = random.randint(1, 100)

def broadcast(message, sender=None):
    with lock:
        for conn in list(players.keys()):
            if conn != sender:
                try:
                    conn.send(message.encode())
                except:
                    conn.close()
                    if conn in players:
                        del players[conn]
                    if conn in scores:
                        del scores[conn]

def handle_player(conn, addr):
    global secret_number

    with lock:
        players[conn] = addr
        scores[conn] = 0

    conn.send("🎯 Welcome to the Number Guessing Game!\nGuess a number between 1 and 100.\nType 'exit' to leave the game.\n".encode())

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode().strip()

            if message.lower() == "exit":
                break

            if not message.isdigit():
                conn.send("❌ Please enter a valid number.\n".encode())
                continue

            guess = int(message)

            if guess == secret_number:
                scores[conn] += 1
                conn.send("✅ Correct! You earned 1 point.\n".encode())
                broadcast(f"🎉 Player {addr} guessed the number right!\n", conn)
                secret_number = random.randint(1, 100)
                broadcast("🔄 New number selected. Guess again!\n")
            elif guess < secret_number:
                conn.send("🔼 Too low! Try again.\n".encode())
            else:
                conn.send("🔽 Too high! Try again.\n".encode())

        except (ConnectionResetError, ConnectionAbortedError):
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            break

    with lock:
        if conn in players:
            del players[conn]
        if conn in scores:
            del scores[conn]

    conn.close()
    print(f"🚪 Player {addr} disconnected.")

# Accept players
while True:
    try:
        conn, addr = server.accept()
        print(f"✅ Player connected from {addr}")
        threading.Thread(target=handle_player, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("🛑 Server shutting down.")
        server.close()
        break
