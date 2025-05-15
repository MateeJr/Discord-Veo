import os

from src import bot
from dotenv import load_dotenv


if __name__ == '__main__':
    # Removed cookie setup for image generation providers
    bot.run_discord_bot()
