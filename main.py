import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix="!")

#This is an event. When the bot is connected to the server, it will notify the general chat that it is online
@bot.event
async def on_ready():
    print('Bunny Bot has arrived!')
    testing_channel = bot.get_channel(int(getenv('TESTING_CHANNEL')))
    await testing_channel.send(f'{bot.user.name} is up and bouncing!')

#This command will shutdown the bot
@bot.command()
async def shutdown(ctx):
    await ctx.reply(f'{bot.user.name} is going to sleep zzz')
    await bot.close()

#this command says Hello! with the respond time
@bot.command(name='1hello')
async def one_hello(ctx):
    await ctx.reply('Hello! ' + str(round(bot.latency * 1000)) + ' ms')

#this command says Howdy Howdy!
@bot.command(name='2hello')
async def two_hello(ctx):
    await ctx.reply('Howdy Howdy!')

#this command adds two numbers and returns the sum
@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)

#this command plays a gif
@bot.command()
async def bunnyjam(ctx):
    await ctx.reply('https://tenor.com/view/bunny-rabbit-vibe-dance-7tv-gif-25070294')

#this command plays a gif
@bot.command()
async def bunnysmile(ctx):
    await ctx.reply('https://i.kym-cdn.com/photos/images/masonry/001/999/882/fe1.gif')

#this command repeats a message without the need of having quotes 
@bot.command()
async def echo(ctx, *, message):
    await ctx.reply(message)

bot.run(getenv('TOKEN'))