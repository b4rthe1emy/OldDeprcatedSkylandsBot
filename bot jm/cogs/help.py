from nextcord.ext import commands
import nextcord
from config import *

class HelpCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@nextcord.slash_command(name='help', guild_ids=[GUILD_ID], description="Display the help menu.")
	async def help(self, interaction: nextcord.Interaction):
		embed = nextcord.Embed(
			title="Aide pour Felix - SkylandMC.fr",
			description="Voici les commandes disponibles pour interagir avec le bot:",
			color=nextcord.Color.blue()
		)
		
		embed.add_field(name="/test", value="descrption.", inline=False)
		
		embed.set_footer(text="Besoin d'assistance supplémentaire ? Contactez notre support via les tickets.")
		
		await interaction.response.send_message(embed=embed, ephemeral=True)

	@commands.command(name='help')
	async def prefix_help(self, ctx):
		embed = nextcord.Embed(
			title="Aide pour Felix - SkylandMC.fr",
			description="Voici les commandes disponibles pour interagir avec le bot:",
			color=nextcord.Color.blue()
		)
		
		embed.add_field(name="/test", value="descrption.", inline=False)
		
		embed.set_footer(text="Besoin d'assistance supplémentaire ? Contactez notre support via les tickets.")
		
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(HelpCog(bot))