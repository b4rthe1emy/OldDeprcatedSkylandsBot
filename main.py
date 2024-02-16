from typing import Final
import discord
from discord.ext import commands
from datetime import datetime

import member_join
import polls

intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


TOKEN: Final[str] = (
    "MTIwNzQ1MDUwOTgzMzY3MDY2Nw.Gy884a.Z7FvKYl60BHGSHJOGY8e3ZskhRnfJfEml6aQkg"
)

# intents: discord.Intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix="/", intents=intents)


polls.setup(client)
member_join.setup(client)


@client.event
async def on_ready():
    date_print(f"{client.user} is running")


if __name__ == "__main__":
    client.run(TOKEN)
