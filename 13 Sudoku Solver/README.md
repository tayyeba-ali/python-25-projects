# 🧩 Sudoku Solver in Python

This project is a simple **backtracking algorithm-based Sudoku Solver** written in Python. Given a 9x9 Sudoku board with empty cells represented by `-1`, it attempts to fill in the missing numbers while following all standard Sudoku rules.

## 📸 Demo

```bash
Input Board (incomplete):
[3, 9, -1, -1, 5, -1, -1, -1, -1]
[-1, -1, -1, 2, -1, -1, -1, -1, 5]
...

Solved Board:
[3, 9, 1, 8, 5, 2, 4, 7, 6]
[8, 6, 7, 2, 4, 1, 9, 3, 5]
...
```

## 🧠 How It Works

The script uses **recursive backtracking** to solve the puzzle:

1. **Find an empty cell** (represented by `-1`).
2. Try a number (1 through 9) in that cell.
3. Check if placing the number is valid:

   * Not already in the row
   * Not already in the column
   * Not already in the 3x3 grid
4. If valid, place the number and **recursively** attempt to solve the rest of the board.
5. If no valid number fits, **backtrack** and try another number.

## 🗾 Features

* Clear and easy-to-read implementation
* Uses Python's `pprint` for clean output
* Well-commented code for learners
* Console output shows whether a solution exists and the filled board

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system

### Run the Program

```bash
python sudoku_solver.py
```

## 🧪 Example Input

```python
example_board = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    ...
]
```

## 📚 Learnings

This project is great for practicing:

* Backtracking algorithms
* Recursive problem solving
* Working with 2D arrays (matrices)
* Sudoku rules enforcement logic

## 🤖 Author

**Tayyeba Ali**
GitHub: [@tayyeba-ali](https://github.com/tayyeba-ali)
