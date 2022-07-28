import discord
from discord.ext import commands

class Requests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #this command says Hello! with the respond time
    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.reply(f'pong {round(self.bot.latency * 1000)} ms')

    #this command says Howdy Howdy!
    @commands.command()
    async def hello(self, ctx):
        await ctx.reply('Howdy Howdy!')

    #this command adds two numbers and returns the sum
    @commands.command()
    async def add(self, ctx, num1:int, num2:int):
        await ctx.reply(num1+num2)

    #this command plays a gif
    @commands.command()
    async def bunnyjam(self, ctx):
        await ctx.reply('https://tenor.com/view/bunny-rabbit-vibe-dance-7tv-gif-25070294')

    #this command plays a gif
    @commands.command()
    async def bunnysmile(self, ctx):
        await ctx.reply('https://i.kym-cdn.com/photos/images/masonry/001/999/882/fe1.gif')


    #this command repeats a message without the need of having quotes 
    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.reply(message)

def setup(bot):
    bot.add_cog(Requests(bot))