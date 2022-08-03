import discord
from youtube_dl import YoutubeDL
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Music(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    is_playing = False
    is_paused = False


    vc = None
    music_queue = []
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}    
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    @commands.command()
    async def play(self, ctx, link):
        ctx.voice_client.stop()
        vc = ctx.voice_client

        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(link, download=False)
            url = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url, **self.FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Song paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Song resumed")

    #This command tells the bot to join the voice channel the user is currently in
    @commands.command()
    async def join(self, ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except Exception as e:
            await ctx.reply("Please make sure you are in a voice channel before calling this command")
            print(e)

    #This command tells the bot to leave the current voice channel
    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))