import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #This is an event. When the bot is connected to the server, it will notify the general chat that it is online
    @commands.Cog.listener() #this is used for events
    async def on_ready(self):
        print('Bunny Bot has arrived!')
        testing_channel = self.bot.get_channel(int(getenv('TESTING_CHANNEL')))
        await testing_channel.send(f'{self.bot.user.name} is up and bouncing!')

    @commands.command() #this is used for commands
    #This command will shutdown the bot
    async def shutdown(self, ctx):
        await ctx.reply(f'{self.bot.user.name} is going to sleep zzz')
        await self.bot.close()

    #this command clear a certain amount of messages (default amount is set to 5)
    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Admin(bot))