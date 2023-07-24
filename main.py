import json
import disnake

from disnake.ext import commands


with open("./config.json", 'r') as file:
    config = json.load(file)

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Бот запущен!")

bot.run(config['TOKEN'])