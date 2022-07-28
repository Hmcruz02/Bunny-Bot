import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

#This class is to create an embedded help command
class MyHelpCommand(commands.HelpCommand):


    async def send_bot_help(self, mapping):
        embed = discord.Embed(title ="Bot Help",
            description = "A list of commands categorized. Use ! before commands",
            colour = discord.Colour.gold())
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/968235354312290314/994066242988150874/brimwaddle.gif')
        #'mapping' is a dict of the bot's cogs and their respective commands
        for cog, cmds in mapping.items():
            if cog is not None:
                
                list_of_commands = ""
                for cmd in cmds:
                    list_of_commands += f'{cmd.name}\n'
                
                embed.add_field(
                    name = cog.qualified_name,
                    value = list_of_commands,
                    inline=False
                )
        embed.set_footer(text="Fluffy Inc.")
        await self.get_destination().send(embed=embed)

bot = commands.Bot(command_prefix="!", help_command= MyHelpCommand())

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

#searches and loads all cogs from the cogs directory
for filename in os.listdir('./BunnyBot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(getenv('TOKEN'))
