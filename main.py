from typing import Final
import discord
from discord.ext import commands
from datetime import datetime

# import member_join
import polls
import private_messages
from skylands_token import TOKEN


intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


intents: discord.Intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


# member_join.setup(client)
polls.setup(bot)
# private_messages.setup(bot)


@bot.event
async def on_ready():
    date_print(f"{bot.user} is running")


if __name__ == "__main__":
    bot.run(TOKEN)
