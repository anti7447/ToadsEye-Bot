from disnake.ext import commands


class On_message(commands.Cog):
    def __init__(self, bot):
        # super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot is True:
            return
        
        print(msg)


def setup(bot):
    bot.add_cog(On_message(bot))
