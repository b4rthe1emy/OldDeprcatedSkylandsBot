import discord
from datetime import datetime

WELCOME_CHANNEL_ID = 1207611571782553653
WELCOME_ROLE_ID = 1207618616623894538


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


def setup(client: discord.Client):

    @client.event
    async def on_member_join(member: discord.Member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel is None:
            return

        print("new member")

        await channel.send(
            embed=discord.Embed(
                colour=0x3498DB,
                title=None,
                description=f"**[NOUVEAU MEMBRE !](<https://skylandsmc.fr>)**\nBienvenue <@{member.id}> sur {member.guild.name}, amuse toi bien !\nTu est le membre #{member.guild.member_count} !",
            )
        )

        welcome_role = member.guild.get_role(WELCOME_ROLE_ID)
        if welcome_role is None:
            return

        try:
            await member.add_roles(welcome_role)
        except:
            pass

    date_print("on_member_join.py loaded succefully")
