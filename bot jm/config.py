import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define commonly used environment variables
GUILD_ID = int(os.getenv('GUILD_ID'))
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_PREFIX = os.getenv('BOT_PREFIX')
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
ADMIN_ROLE_ID = int(os.getenv('ADMIN_ROLE_ID'))
