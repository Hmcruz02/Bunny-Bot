import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix="!")

#loads in an extension
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

#unloads an extension
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

#reloads an extension
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./BunnyBot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(getenv('TOKEN'))