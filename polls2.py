import discord
from discord.ext.commands import Bot
from datetime import datetime


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


def number_emoji(number: int):
    emojis = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    return emojis[number]


def setup(client: discord.Client):

    @client.command(name="poll")
    async def poll(ctx, *options):
        list_options = " ".join(options)
        list_options = list_options.split(";")
        title = list_options[0]
        list_options = list_options[1:]

        formated_options: str = ""
        number = 0
        for option in list_options:
            formated_options += number_emoji(number) + " "
            formated_options += option + "\n"
            number += 1

        msg: discord.Message = await ctx.send(
            embed=discord.Embed(title=title, description=formated_options),
            ephemeral=True,
        )

        number = 0
        for i in range(len(list_options)):
            await msg.add_reaction(number_emoji(i))

    date_print("polls.py loaded succefully")
