from disnake.ext import commands


class On_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

        # DATA_PATH = self.bot.config['data_path']

        # # Создаём файл, если его нет
        # if not os.path.exists(DATA_PATH):
        #     with open(DATA_PATH, 'w') as file:
        #         file.write('{"members": {}}')
        #         file.close()


def setup(bot):
    bot.add_cog(On_ready(bot))