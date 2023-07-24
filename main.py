import disnake
import os
import json

from disnake.ext import commands


with open("./config.json", 'r') as file:
    config = json.load(file)

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Бот запущен!")

# Ищем категории
category_files = [
    f"categories.{category_name[:-3]}"
    for category_name in os.listdir("categories/")
    if category_name.endswith(".py")
]

# Ищем события
event_files = [
    f"events.{event_name[:-3]}"
    for event_name in os.listdir("events/")
    if event_name.endswith(".py")
]

# Загружаем категории
for category_file in category_files:
    try:
        bot.load_extension(category_file)
    except Exception as err:
        print(err)

# Загружаем события
for event_file in event_files:
    try:
        bot.load_extension(event_file)
    except Exception as err:
        print(err)

bot.run(config['TOKEN'])