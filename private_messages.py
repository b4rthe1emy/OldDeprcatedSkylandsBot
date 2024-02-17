import discord
from datetime import datetime
from discord.ext.commands import Bot


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


def setup(bot: Bot):

    date_print("private_messages.py loaded succefully")
