# 🔠 Hangman Game (Python)

A command-line version of the classic **Hangman** game built using Python! Guess the word one letter at a time before the stick figure is fully drawn!

---

## 🎮 How to Play

* A random word is chosen from a predefined word list.
* The player guesses letters one by one.
* If the guessed letter is in the word, it's revealed in the correct position(s).
* If the guessed letter is wrong, you lose one life.
* You have 7 lives before the hangman is complete and the game is over.

---

## 📦 Project Files

* `main.py` – Game logic
* `words.py` – List of words to choose from
* `hangman_visual.py` – ASCII art visuals for each life stage stored as `lives_visual_dict`

---

## 🧠 Concepts Used

* `random.choice()`
* Sets and string manipulation
* User input validation
* ASCII art for terminal UI

---

## ▶️ How to Run

1. Make sure you have `main.py`, `words.py`, and `hangman_visual.py` in the same directory.
2. Run the script:

```bash
python main.py
```

3. Start guessing letters!

---

## 📜 Sample Output

```
You have 7 lives left and you have used these letters:
Current word:  - - - - -
Guess a letter: e
Your letter, E is not in the word.
```

---

## 🧩 Example Structure for `words.py`

```python
words = ['python', 'developer', 'hangman', 'programming', 'challenge']
```

---

## 🎨 Example ASCII Art in `hangman_visual.py`

```python
lives_visual_dict = {
    7: '',
    6: '...',
    0: '''
       ___________
      | /        |
      |/        ( )
      |          |
      |         / \
      |
    '''
}
```

---

## 👩‍💻 Author

**Tayyeba Ali** — Coding with creativity and fun one project at a time! 😊

---

Get ready to guess smart and survive the hangman! 🪢
