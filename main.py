import discord
from discord.ext import commands

# import member_join
import polls
from skylands_token import TOKEN
from prints import debug

intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


intents: discord.Intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


# member_join.setup(client)
polls.setup(bot)
# private_messages.setup(bot)


@bot.event
async def on_ready():
    debug(f"{bot.user} is running")


if __name__ == "__main__":
    bot.run(TOKEN)
