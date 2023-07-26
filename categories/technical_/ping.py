from disnake.ext import commands
from disnake import ApplicationCommandInteraction
from categories.technical import Techical


class Ping(Techical):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.slash_command(name="пинг", description="Русское описание")
    async def ping(self, inter: ApplicationCommandInteraction):
        await inter.response.send_message(content=f"Pong *{round(self.bot.latency * 100, 2)} ms*.")


def setup(bot):
    bot.add_cog(Ping(bot))