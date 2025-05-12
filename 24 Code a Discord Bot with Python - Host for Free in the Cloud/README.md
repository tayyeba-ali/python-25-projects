# 🤖 Discord Encouragement Bot

A Discord bot that sends inspirational quotes and custom encouraging messages. Built with Python and the Discord API.

---

## 🌟 Features
- Responds to sad keywords with encouragements
- Sends a random quote using `$inspire`
- Add custom encouragements using `$new <message>`
- Delete custom encouragements using `$del <index>`
- List all custom encouragements with `$list`
- Keeps itself alive using Flask (great for free hosting like Repl.it)

---

## 🚀 Getting Started

### 📁 Requirements
- Python 3.8+
- `discord.py`
- `requests`
- `python-dotenv`
- `flask`

Install dependencies:
```bash
pip install -r requirements.txt
```

### 🛠️ Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/your-bot-repo.git
cd your-bot-repo
```

2. Create a `.env` file:
```env
TOKEN=your_discord_bot_token_here
```

3. Run the bot:
```bash
python main.py
```

---

## 🔧 Bot Commands
| Command | Description |
|---------|-------------|
| `$inspire` | Sends a random inspirational quote |
| `$new <message>` | Adds a new encouraging message |
| `$del <index>` | Deletes an encouraging message by index |
| `$list` | Lists all custom encouragements |

---

## 🧠 How It Works
- Uses `zenquotes.io` API for inspirational quotes
- Saves custom encouragements to a JSON file
- Keeps bot alive with Flask server (`keep_alive`)

---

## 📂 File Structure
```
├── encouragements.json       # Stores custom messages
├── keep_alive.py             # Flask server for uptime
├── main.py                   # Main bot logic
├── .env                      # Environment variables (token)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 📜 License
This project is licensed under the MIT License.

---

Made with ❤️ by Tayyeba
