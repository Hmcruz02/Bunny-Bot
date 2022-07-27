import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #This is an event. When the bot is connected to the server, it will notify the server that it is online
    #and that status
    @commands.Cog.listener() #this is used for events
    async def on_ready(self):
        print('Bunny Bot has arrived!')
        await self.bot.change_presence(activity=discord.Game('Valorant'))
        testing_channel = self.bot.get_channel(int(getenv('TESTING_CHANNEL')))
        await testing_channel.send(f'{self.bot.user.name} is up and bouncing!')

    #this sends a message if an error occurs
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command is not found.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all required Arguments.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to use this command.')
        else:
            await ctx.send('An Error has occured.')

    @commands.command() #this is used for commands
    #This command will shutdown the bot
    async def shutdown(self, ctx):
        await ctx.reply(f'{self.bot.user.name} is going to sleep zzz')
        await self.bot.close()

    #this command clear a certain amount of messages (default amount is set to 5)
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Admin(bot))