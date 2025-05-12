import discord
import os
from dotenv import load_dotenv
import requests
import json
import random
from keep_alive import keep_alive

load_dotenv()

# File to store encouragements locally
ENCOURAGEMENTS_FILE = "encouragements.json"

# Initialize encouragements file if it doesn't exist
if not os.path.exists(ENCOURAGEMENTS_FILE):
    with open(ENCOURAGEMENTS_FILE, "w") as f:
        json.dump([], f)

def load_encouragements():
    try:
        with open(ENCOURAGEMENTS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading encouragements: {e}")
        return []

def save_encouragements(encouragements):
    try:
        with open(ENCOURAGEMENTS_FILE, "w") as f:
            json.dump(encouragements, f)
        return True
    except Exception as e:
        print(f"Error saving encouragements: {e}")
        return False

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "You are a great person!",
    "Hang in there.",
    "Stay positive!",
    "You're doing amazing 💖"
]

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        json_data = json.loads(response.text)
        quote = f"{json_data[0]['q']} — {json_data[0]['a']}"
        return quote
    except Exception as e:
        print(f"Error getting quote: {e}")
        return random.choice(starter_encouragements)

def update_encouragements(encouraging_message):
    encouragements = load_encouragements()
    encouragements.append(encouraging_message)
    return save_encouragements(encouragements)

def delete_encouragement(index):
    encouragements = load_encouragements()
    if 0 <= index < len(encouragements):
        del encouragements[index]
        return save_encouragements(encouragements)
    return False

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    try:
        if msg.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)

        elif msg.startswith('$new'):
            encouraging_message = message.content.split('$new ', 1)[1]
            if update_encouragements(encouraging_message):
                await message.channel.send("✅ New encouraging message added.")
            else:
                await message.channel.send("❌ Failed to add message.")

        elif msg.startswith('$del'):
            parts = message.content.split('$del ', 1)
            if len(parts) == 2 and parts[1].isdigit():
                index = int(parts[1])
                if delete_encouragement(index):
                    await message.channel.send("🗑️ Encouraging message deleted.")
                else:
                    await message.channel.send("❌ Invalid index.")
            else:
                await message.channel.send("❌ Please provide a valid index.")

        elif msg.startswith('$list'):
            encouragements = load_encouragements()
            if encouragements:
                await message.channel.send("\\n".join(
                    f"{i}: {enc}" for i, enc in enumerate(encouragements)
                ))
            else:
                await message.channel.send("No custom encouragements found.")

        elif any(word in msg for word in sad_words):
            options = starter_encouragements + load_encouragements()
            if options:
                await message.channel.send(random.choice(options))

    except Exception as e:
        print(f"Error processing message: {e}")
        await message.channel.send("❌ An error occurred. Please try again.")

keep_alive()
token = os.getenv("TOKEN")
if token is None:
    print("❌ Error: Discord bot TOKEN not found!")
    print("Please add your Discord bot token in the Secrets tab (Tools > Secrets)")
    print("Create a new secret with key 'TOKEN' and your bot token as the value")
    exit(1)
client.run(token)
