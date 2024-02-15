import discord
from datetime import datetime
from discord.ext.commands import Bot

WELCOME_CHANNEL_ID = 1207611571782553653
WELCOME_ROLE_ID = 1207618616623894538


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


def setup(bot: Bot):

    @bot.event
    async def on_member_join(member: discord.Member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel is None:
            return

        print("new member")

        await channel.send(f"Bienvenue <@{member.id}> sur {member.guild.name} !")

        welcome_role = member.guild.get_role(WELCOME_ROLE_ID)
        if welcome_role is None:
            return

        try:
            await member.add_roles(welcome_role)
            await channel.send(
                f"On t'a préparé le rôle <@&{WELCOME_ROLE_ID}> juste pour toi ! Amuse toi bien sur {member.guild.name}"
            )
        except:
            pass

    date_print("on_member_join.py loaded succefully")
    return bot
