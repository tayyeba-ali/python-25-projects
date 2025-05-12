# 🧠 Markov Chain Text Composer

A Python project that generates random yet coherent text using Markov Chains. Great for creative writing, bot content, or fun random sentence generation!

---

## 🌟 Features
- Trains on sample text to build a word-level Markov chain
- Generates new text that mimics the style of the input
- Configurable chain depth
- Lightweight and easy to extend

---

## 🚀 Getting Started

### 📁 Requirements
- Python 3.6+

Install dependencies:
```bash
pip install -r requirements.txt
```

### 🛠️ Setup & Run
1. Clone the repository:
```bash
git clone https://github.com/your-username/markov-text-composer.git
cd markov-text-composer
```

2. Run the composer:
```bash
python composer.py
```

3. Input your training text when prompted, or load from a file.

---

## ⚙️ How It Works
- Reads input text and creates a Markov chain dictionary
- Randomly selects a starting word and builds a sequence based on probabilities
- Depth determines how many previous words are considered for the next prediction

---

## 📂 File Structure
```
├── composer.py              # Main logic for Markov chain
├── sample.txt               # Optional input training file
├── requirements.txt         # Python dependencies
└── README.md                # Documentation
```

---

## 📜 License
MIT License

---

Made with ❤️ by Tayyeba
