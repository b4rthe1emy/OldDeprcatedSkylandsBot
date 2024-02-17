import discord
from datetime import datetime
from discord.ext import commands
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

    @bot.command(name="poll")
    async def poll(context: commands.Context):
        try:
            if context.message.author.get_role(ADMIN_ROLE_ID) is None:
                await context.reply(
                    f"Uniquement les admistraturs peuvent envoyer des sondages.",
                    silent=True,
                    reference=context.message,
                )
                return
        except Exception:
            pass

        options: str = context.message.content[6:]

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

        poll_message: discord.Message = await context.reply(
            embed=discord.Embed(
                title=title,
                description=formated_options,
                colour=0x3498DB,
            ),
            view=view(int(poll_id)),
        )

        poll_votes.create_poll(poll_message, int(poll_id), len(list_options))

        await context.message.delete()

    @bot.command(name="poll_list")
    async def poll_list(context: commands.Context):
        polls = "\n".join([str(p) for p in poll_votes.polls])
        await context.reply(f"```\n{polls}\n```")

    @bot.command(name="poll_results")
    async def poll_results(context: commands.Context):
        try:
            poll_id = int(context.message.content[14:])
        except:
            await context.reply(
                f"{context.message.content[14:]} n'est pas une id valide.",
                ephemeral=True,
            )
            await context.message.delete()
            return

        poll = poll_votes.find_poll(poll_id)
        poll_votes.polls.remove(poll)
        await context.reply(poll.votes)

    date_print("polls.py loaded succefully")
