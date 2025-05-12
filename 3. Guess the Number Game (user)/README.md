# 🧠 Guess the Number Game (User vs Computer & Computer vs User)

This Python script includes **two fun number guessing games**:

1. **User guesses the number** picked by the computer
2. **Computer guesses the number** you're thinking of!

---

## 🎮 Game Modes

### 1. User Guesses the Number

* The computer randomly selects a number between 1 and `x`
* The user guesses until they get it right
* The game gives hints if the guess is too high or too low

### 2. Computer Guesses the Number

* You think of a number between 1 and `x`
* The computer keeps guessing until it gets it right
* You provide feedback: `H` (Too High), `L` (Too Low), or `C` (Correct)

---

## 📜 Example Output

```
Is 5 too high (H), too low (L), or correct (C)? L
Is 7 too high (H), too low (L), or correct (C)? C
Yay! The computer guessed your number, 7, correctly!
```

---

## 🧠 Concepts Practiced

* Random number generation
* Conditionals and loops
* Functions and user input

---

## ▶️ How to Run

1. Save as `guess_game.py`
2. Run in terminal:

```bash
python guess_game.py
```

3. Call `guess(x)` or `computer_guess(x)` depending on the mode you want to play.

---

## ⚠️ Note

Fix a small print bug:

```python
print(f"Yay, Congratulations. You have guessed the number {random_num} correctly ")
```

(Use `f` before the string for variable interpolation.)

---

## 👩‍💻 Author

**Tayyeba Ali** — Creating smart and fun Python games for all levels! 😊

---

Challenge yourself or challenge the computer — happy guessing! 🎲
