import discord
from discord.ext import commands
from prints import *
from parameters import *


def get_pastille(status):
    if status == "online":
        return "🟢"
    if status == "maint":
        return "🟠"
    if status == "offline":
        return "🔴"


def setup(bot: commands.Bot):
    @bot.command(name="set_status")
    async def set_status(context: commands.Context):
        if context.message.author.get_role(ADMIN_ROLE_ID) is None:
            await context.reply(f"Uniquement les administrateurs")

        status = context.message.content[12:]

        if status not in ["online", "offline", "maint"]:
            await context.reply(f"Le status {status} n'est pas un status disponible.")
            return

        file = open("status.txt", "wt")
        file.write(status)
        debug("status: " + status)
        debug("written to status.txt")

        channel = context.message.guild.get_channel(STATUS_CHANNEL_ID)
        pastille = get_pastille(status)
        channel_name = f"『{pastille}』𝐒𝐭𝐚𝐭𝐮𝐬"

        await channel.purge(reason="test aaa")
        await channel.edit(name=channel_name)
        await channel.send(status)

    load("status.py", "loaded succefully")
