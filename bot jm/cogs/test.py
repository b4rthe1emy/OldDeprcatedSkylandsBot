import re
from nextcord.ext import commands
import nextcord
from nextcord.interactions import Interaction
from config import *

class APIKeyModal(nextcord.ui.Modal):
	def __init__(self):
		super().__init__("Test Modal", "Description", color=nextcord.Color.blurple())
		
		self.api_key_input = nextcord.ui.TextInput(label="Yolo", min_length=32, max_length=55, required=True, placeholder="yoyo")
		self.add_item(self.api_key_input)
			
	async def callback(self, interaction: nextcord.Interaction) -> None:
			api_key = self.api_key_input.value

			await interaction.response.send_message("gg !", ephemeral=True)

class TestCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@nextcord.slash_command(name='Test Modal', guild_ids=[GUILD_ID], description="Description.")
	async def link(self, interaction: nextcord.Interaction):
		await interaction.response.send_modal(APIKeyModal())	

def setup(bot):
	bot.add_cog(TestCog(bot))
