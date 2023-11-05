#https://realpython.com/how-to-make-a-discord-bot-python/

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    # Prints message when the bot goes online.
    print(f'{client.user} has connected to Discord!')