import discord
from discord.ext import commands

import polls
import status

from skylands_token import TOKEN
from prints import *

intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


intents: discord.Intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


polls.setup(bot)
status.setup(bot)


@bot.event
async def on_ready():
    online(f"{bot.user}", "is running")


if __name__ == "__main__":
    bot.run(TOKEN)
