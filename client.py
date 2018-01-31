#Does nothing work these days? Report issues of the bot in the issues tab.
import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix= "bot_prefix_here"
Client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
print Github https://github.com/GirGir/Client-Discord.py-Bot

@client.event
async def on_message(message):
    if message.content == "commandhere":
        await client.send_message(message.channel, "messagehere")
   
client.run("token")
