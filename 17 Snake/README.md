# 🐍 Snake Game in Python

This is a classic Snake Game implemented in Python using the `pygame` library for rendering and `tkinter` for displaying game-over messages. The game features a grid-based snake that grows when it eats snacks and ends when the snake collides with itself.

---

## 🎮 Features

* Snake movement using arrow keys
* Edge wrapping (snake appears from the opposite side)
* Random snack placement
* Snake growth on snack consumption
* Game-over message with score

---

## 🧰 Technologies Used

* Python 3
* `pygame` - for rendering graphics and handling events
* `tkinter` - for displaying the game-over message box

---

## 📦 How to Run

1. **Install dependencies:**

   ```bash
   pip install pygame
   ```

2. **Run the game:**

   ```bash
   python snake_game.py
   ```

---

## 🎮 Controls

* `←` Arrow Left: Move left
* `→` Arrow Right: Move right
* `↑` Arrow Up: Move up
* `↓` Arrow Down: Move down

---

## 🚀 Game Mechanics

* The snake moves continuously in the current direction.
* Arrow keys change the snake's direction.
* If the snake eats the green snack, it grows.
* If the snake runs into itself, a game-over message is displayed.
* The game restarts automatically after a collision.

---

## 📈 Scoring

* The score is the length of the snake.
* The score is printed in the console when the game ends.

---

## 🙌 Credits

Developed as a Python practice project using `pygame` and `tkinter`.

---

Enjoy coding and have fun playing! 🕹️
