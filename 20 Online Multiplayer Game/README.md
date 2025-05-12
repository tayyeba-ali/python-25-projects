# 🎯 Multiplayer Number Guessing Game

Welcome to the **Multiplayer Number Guessing Game** built with Python's socket and threading libraries! This game allows multiple players to connect to a server and guess a randomly generated number between 1 and 100.

---

## 🛠️ Features

* Real-time multiplayer gameplay
* Server broadcasts messages to all players
* Players earn points for correct guesses
* Automatic number reset after a correct guess
* Graceful handling of disconnections

---

## 🚀 How It Works

1. The server listens for connections on port `5555`.
2. Clients can connect to the server and start guessing.
3. When a player guesses the correct number:

   * They earn a point.
   * The server announces the winner to all other players.
   * A new number is generated.
4. Players can exit anytime by typing `exit`.

---

## 🖥️ Setup Instructions

### 1. Clone the Repository (if applicable)

```bash
# git clone <your-repo-url>
```

### 2. Run the Server

```bash
python server.py
```

### 3. Run the Client(s)

```bash
python client.py
```

You can run multiple clients in different terminal windows.

---

## 📁 Files

* `server.py`: The main server-side logic.
* `client.py`: The player client that connects to the server.

---

## ⚙️ Requirements

* Python 3.x

No external libraries are required.

---

## 🧠 Future Improvements

* Add a scoreboard broadcast
* Support chat messages between players
* WebSocket version for browser-based play

---

## 👩‍💻 Author

**Tayyeba Ali** — Passionate about learning and building Python-based multiplayer games! 😊

---

Enjoy the game and happy guessing! 🎉
