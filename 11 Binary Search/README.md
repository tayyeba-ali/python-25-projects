# Binary vs Naive Search in Python

This Python script demonstrates the difference in efficiency between **binary search** and **naive (linear) search** algorithms.

## 🧠 Concepts

* **Naive Search**: Goes through each element one by one until it finds the target. Time complexity: `O(n)`.
* **Binary Search**: Exploits the sorted nature of the list by repeatedly dividing the search space in half. Time complexity: `O(log n)`.

## 🚀 Features

* Compares both search algorithms on a randomly generated sorted list.
* Measures and prints the average time taken for each search algorithm.
* Educational tool to demonstrate why algorithm choice matters in practice.

## 📁 File Structure

```
binary_search_vs_naive.py  # Main implementation script
```

## ▶️ How to Run

Make sure you have Python installed. Then run:

```bash
python binary_search_vs_naive.py
```

You will see output like:

```
Naive Search time:  0.00005 seconds
Binary Search time:  0.000003 seconds
```

## 🔍 Example Functions

* `naive_search(l, target)`
* `binary_search(l, target, low=None, high=None)`

## 📌 Notes

* The list is randomly generated with unique integers.
* The binary search only works on **sorted** lists.
* The difference in performance becomes significant for large lists.

## 🏁 License

This project is for educational purposes.

---

By @tayyeba-ali
