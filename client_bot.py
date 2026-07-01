""" $hello
$bye
$passw
$dado """

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot_logic import gen_pass

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}!")

@bot.command()
async def bye(ctx):
    await ctx.send("Chao con adiós🙂")

@bot.command()
async def passw(ctx):
    await ctx.send("Tu contraseña: " + gen_pass(10))

@bot.command()
async def dado(ctx):
    import random
    await ctx.send(f"En el dado salió: {random.randint(1, 6)}")

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f"images/{img_name}", "rb") as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def contaminacion(ctx):
    img_name = random.choice(os.listdir("Contaminacion"))
    with open(f"Contaminacion/{img_name}", "rb") as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run(TOKEN)