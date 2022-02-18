from pony import orm

from discord import Embed

from discord import Message
from discord.ext.tasks import loop
from discord.ext.commands import Bot, Cog

from src.utils import get_current_time
from src.database import App_AdsForEmployee, App_Channel


class AdsSender(Cog):
    
    def __init__(self: "AdsSender", bot: Bot) -> None:
        self.bot = bot
        self._send_ads.start()

    @loop(seconds=10)
    async def _send_ads(self: "AdsSender") -> None:
        with orm.db_session:
            ads = orm.select(
                a for a in App_AdsForEmployee 
                if a.date_of_publication <= get_current_time()
            )

            for channel in App_Channel.select():
                for ad in ads:
                    embed = Embed(title=ad.name, description=ad.description)
                    message: Message = await self.bot.get_channel(int(channel.channel_id)).send(embed=embed)
                    
                    if ad.type == 2:
                        await message.add_reaction('✅')
                        await message.add_reaction('❌')

                    ad.delete()

    @_send_ads.before_loop
    async def _before_send_ads(self):
        print("AdsSender is starting")
        await self.bot.wait_until_ready()


def setup(bot: Bot) -> None:
    bot.add_cog(AdsSender(bot))
