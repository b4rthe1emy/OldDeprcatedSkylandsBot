import discord
from datetime import datetime
from discord.ext import commands

ADMIN_ROLE_ID = 1208047074558345227


def date_print(*args):
    print(f"{datetime.now():%c}", *args)


def number_emoji(number: int):
    emojis = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    return emojis[number]


import polls_buttons
import poll_votes


def setup(bot: commands.Bot):

    @bot.event
    async def on_message(message: discord.Message):
        if message.author == bot.user:
            return

        if not message.content.startswith("/poll "):
            return

        if message.author.get_role(ADMIN_ROLE_ID) is None:
            await message.channel.send(
                f"Uniquement les admistraturs peuvent envoyer des sondages.",
                silent=True,
                reference=message,
            )
            return

        options: str = message.content[6:]

        list_options = options.split(";")
        title = list_options[1]
        poll_id = list_options[0]
        list_options = list_options[2:]

        formated_options: str = ""
        number = 0
        for option in list_options:
            formated_options += number_emoji(number) + " "
            formated_options += option + "\n"
            number += 1

        view = polls_buttons.get_view(len(list_options))

        poll_message: discord.Message = await message.channel.send(
            embed=discord.Embed(
                title=f"[POLL_ID={poll_id}] " + title,
                description=formated_options,
                colour=0x3498DB,
            ),
            view=view(poll_id),
        )

        poll_votes.create_poll(poll_message, poll_id)

        await message.delete()

    date_print("polls.py loaded succefully")
