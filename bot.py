import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
  
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
        
discord_token = os.environ["DISCORD_SCRAPER_API_KEY"]
print(discord_token)
client.run(discord_token)
