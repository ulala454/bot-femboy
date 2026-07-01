import os
import discord
from dotenv import load_dotenv
from bot_logic import gen_pass

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hemos iniciado sesión como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hi!")

    elif message.content.startswith("$bye"):
        await message.channel.send("\U0001f642")

    elif message.content.startswith("$pass"):
        await message.channel.send("Tu contraseña: " + gen_pass(10))

    else:
        await message.channel.send("No entendí el comando.")

client.run(TOKEN)