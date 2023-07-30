import datetime
import disnake

from disnake import ApplicationCommandInteraction
from disnake import Member
from disnake import Embed

from disnake.ext import commands

from categories.moderation import Moderation


class Mute(Moderation):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.slash_command(name="мьют", description="Русское описание")
    @commands.has_guild_permissions(moderate_members=True)
    async def mute(self, inter: ApplicationCommandInteraction,
                   target_member: Member = commands.Param(name="пользователь", description="Кого заквачить?"),
                   duration_mute: int = commands.Param(default=40320, name="время", description="Продолжительность мьюта"),
                   unit: str = commands.Param(default="Минут", name="система", description="Единица измерения времени (часы, минуты и т. д.)", autocomplete=[
                       "Секунд",
                       "Минут",
                       "Часов",
                       "Дней",
                       "Недель"
                   ]),
                   reason: str = commands.Param(default="без причины", name="причина", description="Кого заквачить?")
                   ):
        # await inter.response.send_message(content=f"Pong *{round(self.bot.latency * 100, 2)} ms*. {target_member}")
        first_date = datetime.datetime(year=1970, day=1, month=1, hour=3)
        time_since = datetime.datetime.now() - first_date
        seconds = int(time_since.total_seconds())

        try:

            duration_time = unit # duration = 1h. [:0] = h
            duration_timer = None # timedelta

            if unit == "Секунд":
                if duration_mute > 2419200:
                    duration_mute = 2419200
                duration_timer = duration_mute # datetime.datetime.utcnow() + datetime.timedelta(hours=3, seconds=duration_mute)
            if unit == "Минут":
                if duration_mute > 40320:
                    duration_mute = 40320
                duration_timer = duration_mute * 60 # datetime.datetime.utcnow() + datetime.timedelta(hours=3, minutes=duration_mute)
            if unit == "Часов":
                if duration_mute > 672:
                    duration_mute = 672
                duration_timer = duration_mute * 60 * 60 # datetime.datetime.utcnow() + datetime.timedelta(hours=duration_mute+3)
            if unit == "Дней":
                if duration_mute > 28:
                    duration_mute = 28
                duration_timer = duration_mute * 60 * 60 * 24 # datetime.datetime.utcnow() + datetime.timedelta(hours=3, days=duration_mute)
            if unit == "Недель":
                if duration_mute > 4:
                    duration_mute = 4
                duration_timer = duration_mute * 60 * 60 * 24 * 7 # datetime.datetime.utcnow() + datetime.timedelta(hours=3, weeks=duration_mute)

            await target_member.timeout(duration=duration_timer, reason=reason)

            embed = Embed(
                title="Пользователь замучен",
                color=0x00ff00,
                description=f"Вы, модератор {inter.author.display_name} ({inter.author.mention}), замьютили {target_member.display_name} ({target_member.mention}) на {duration_mute}{unit[0]} по причине\n> {reason}\n\nМьют продлится до <t:{seconds + duration_timer}:f>"
            )
            await inter.response.send_message(embed=embed)

            
        except disnake.Forbidden:
            embed = Embed(
                title="Ошибка",
                color=0xff0000,
                description="У меня недостаточно прав для выполнения этой команды."
            )
            await inter.response.send_message(embed=embed, ephemeral=True)

        except commands.MissingPermissions:
            embed = Embed(
                title="Ошибка",
                color=0xff0000,
                description="У вас недостаточно прав для выполнения этой команды."
            )
            await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Mute(bot))