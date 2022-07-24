import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix="!")

@bot.command(name='1hello')
async def one_hello(ctx):
    await ctx.reply('Hello!')

@bot.command(name='2hello')
async def two_hello(ctx):
    await ctx.reply('Howdy Howdy!')

@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)

@bot.command()
async def bunnyjam(ctx):
    await ctx.reply('https://tenor.com/view/bunny-rabbit-vibe-dance-7tv-gif-25070294')

@bot.command()
async def bunnysmile(ctx):
    await ctx.reply('https://i.kym-cdn.com/photos/images/masonry/001/999/882/fe1.gif')
    
bot.run(getenv('TOKEN'))