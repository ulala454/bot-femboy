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
async def contaminacion(ctx):
    await ctx.send(f"La contaminación daña el aire, el agua y la tierra, poniendo en riesgo la salud y el equilibrio del planeta. Cuidar el ambiente es responsabilidad de todos. {bot.user}!")

@bot.command()
async def bye(ctx):
    await ctx.send("Chao,recuerda cuidar el ambiente🙂")

@bot.command()
async def passw(ctx):
    await ctx.send("Tu contraseña: " + gen_pass(10))

@bot.command()
async def animales(ctx):
    import random
    await ctx.send(f"este es el numero de animales que tendrias que salvar: {random.randint(1, 6)}")

@bot.command()
async def devastacion(ctx):
    img_name = random.choice(os.listdir("Contaminacion"))
    with open(f"Contaminacion/{img_name}", "rb") as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run(TOKEN)