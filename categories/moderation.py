from disnake.ext import commands
import os

class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

def setup(bot):

    # Ищем команды этой категории
    command_files = [
        f"categories.moderation_.{command_name[:-3]}"
        for command_name in os.listdir("categories/moderation_/")
        if command_name.endswith(".py")
    ]

    # Загружаем категории
    for command_file in command_files:
        try:
            bot.load_extension(command_file)
        except Exception as err:
            print(err)