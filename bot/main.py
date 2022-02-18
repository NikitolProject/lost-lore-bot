import os

from discord import Intents
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from dotenv import load_dotenv

load_dotenv('.env')

bot = Bot(command_prefix="!", self_bot=True, intents=Intents.default())
slash = SlashCommand(bot)

bot.load_extension("src.workers.ads_sender")
bot.run(os.getenv("DISCORD_TOKEN"))
