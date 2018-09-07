import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready")
    
@client.event
async def on_message(message):
    if message.content == "#roll":
        await client.send_message(message.channel, "(0.author.mention) :cookie:")

client.run("NDg3NjA3Mjg0NTU0NTMwODI2.DnQwhw.pgtEQYlOso9tBqW9K9UnfJn9C_Y")
