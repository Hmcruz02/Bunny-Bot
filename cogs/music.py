import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Music(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test(self, ctx):
        await ctx.reply("This is a test command for Music Cog")
    
    @commands.command()
    async def join(self, ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except Exception as e:
            await ctx.reply("Please make sure you are in a voice channel before calling this command")
            print(e)


    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))