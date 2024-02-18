import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from rich import print
import traceback
from nextcord.ui import Button, View
from nextcord.ui.button import button
from nextcord import ButtonStyle
from config import *


# Crée une instance du bot avec un préfixe pour les commandes
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
	print(f"[green]Bot connecté en tant que {bot.user.name} (ID: {bot.user.id})[/green]")

# Charger les cogs depuis le dossier "cogs"
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')
		print(f"[blue]Cog {filename} chargé.[/blue]")

# Ajoutez d'autres commandes et événements ici

# Bouton de suppression
class DeleteView(View):
	def __init__(self, admin_role_id: int):
		super().__init__(timeout=None)
		self.admin_role_id = admin_role_id

	@button(label="Supprimer", style=ButtonStyle.red)
	async def delete_button(self, button: Button, interaction: nextcord.Interaction):
		# Vérifiez si l'utilisateur a le rôle d'administrateur
		if self.admin_role_id in [role.id for role in interaction.user.roles]:
			await interaction.message.delete()
		else:
			await interaction.response.send_message("Vous n'avez pas la permission de supprimer ce message.", ephemeral=True)

# Gestion des erreurs
@bot.event
async def on_command_error(ctx, error):
	try:
		print("Erreur détectée ! En train d'envoyer l'embed...")

		# Obtient l'objet channel où envoyer le rapport d'erreur
		error_channel = bot.get_channel(LOG_CHANNEL)  
		
		# Crée un embed pour le rapport d'erreur
		embed = nextcord.Embed(title="🔴 Une Erreur s'est produite !", color=nextcord.Color.red())
		embed.add_field(name="Commande", value=f"`{ctx.command}`", inline=False)
		embed.add_field(name="Erreur", value=f"```{type(error).__name__}: {str(error)}```", inline=False)
		
		# Pour des erreurs plus détaillées, vous pouvez utiliser traceback
		tb = traceback.format_exception(type(error), error, error.__traceback__) 
		embed.add_field(name="Détail de l'Erreur", value="```" + "".join(tb)[-1000:] + "```", inline=False)

		# Ajoute une horodatage et une icône pour l'embed
		embed.set_footer(text="Erreur détectée à")
		embed.timestamp = nextcord.utils.utcnow()

		# Créez une vue avec le bouton de suppression en utilisant ADMIN_ROLE_ID
		view = DeleteView(ADMIN_ROLE_ID)

		# Envoie l'embed au canal d'erreurs avec la vue
		await error_channel.send(embed=embed, view=view)
		print("Embed envoyé avec le bouton de suppression !")
	except Exception as e:
		print(f"Erreur lors de l'envoi de l'embed : {e}")


@bot.event
async def on_application_command_error(ctx, error):
	try:
		print("Erreur détectée ! En train d'envoyer l'embed...")

		# Obtient l'objet channel où envoyer le rapport d'erreur
		error_channel = bot.get_channel(LOG_CHANNEL)  
		
		# Crée un embed pour le rapport d'erreur
		embed = nextcord.Embed(title="🔴 Une Erreur s'est produite !", color=nextcord.Color.red())
		command_name = ctx.data['name']
		embed.add_field(name="Commande", value=f"`{command_name}`", inline=False)

		embed.add_field(name="Erreur", value=f"```{type(error).__name__}: {str(error)}```", inline=False)
		
		# Pour des erreurs plus détaillées, vous pouvez utiliser traceback
		tb = traceback.format_exception(type(error), error, error.__traceback__) 
		embed.add_field(name="Détail de l'Erreur", value="```" + "".join(tb)[-1000:] + "```", inline=False)

		# Ajoute une horodatage et une icône pour l'embed
		embed.set_footer(text="Erreur détectée à")
		embed.timestamp = nextcord.utils.utcnow()

		# Créez une vue avec le bouton de suppression en utilisant ADMIN_ROLE_ID
		view = DeleteView(ADMIN_ROLE_ID)

		# Envoie l'embed au canal d'erreurs avec la vue
		await error_channel.send(embed=embed, view=view)
		print("Embed envoyé avec le bouton de suppression !")
	except Exception as e:
		print(f"Erreur lors de l'envoi de l'embed : {e}")


# Une commande pour tester on_command_error
@bot.command(name='test_error')
async def test_error(ctx):
	"""Une commande pour générer une erreur et tester on_command_error."""
	raise ValueError("Ceci est une erreur de test.")

# Lance le bot
bot.run(TOKEN)
