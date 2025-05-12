# Minesweeper in Python

This is a command-line implementation of the classic **Minesweeper** game written in Python.

## 🧠 How It Works

* A board is created with a specified number of bombs randomly distributed.
* The player digs at locations on the board attempting to avoid bombs.
* If a bomb is uncovered, the game is over.
* If an empty cell (with 0 neighboring bombs) is dug, neighboring cells are automatically uncovered (recursive digging).

## 🎮 Gameplay Instructions

* Run the game with:

  ```bash
  python minesweeper.py
  ```
* You'll be prompted to enter coordinates to dig in the format:

  ```
  row,col
  ```
* Keep digging until all safe spots are uncovered to win!

## 📦 Features

* Customizable board size and bomb count.
* Recursive digging for cells with no nearby bombs.
* Automatically updates and shows the board after every move.
* Robust input validation and user guidance.

## 🔧 Code Overview

* `Board` class:

  * `make_new_board()` – initializes the board and plants bombs.
  * `assign_values_to_board()` – assigns numbers indicating nearby bombs.
  * `dig()` – processes user moves and handles recursion.
  * `__str__()` – displays the current state of the board.
* `play()` – handles the game loop and user input.

## ✅ Example

```
   0  1  2  3  4  5  6  7  8  9
0 |   |   |   |   |   |   |   |   |   |   |
1 |   |   |   |   |   |   |   |   |   |   |
...
Where would you like to dig? (row,col): 2,3
```

## 📁 File Structure

```
minesweeper.py
README.md
```

## 🚀 Future Improvements

* GUI version using Tkinter or Pygame.
* Timer and high score system.
* Flagging suspected bombs.

## 👩‍💻 Author

**Tayyeba Ali**
A passionate Python developer creating engaging projects to learn and grow. 😊

---

Enjoy the game! 🧨
