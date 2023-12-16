import random
import discord
from discord.ext import commands

TOKEN = ""
WELcome_CHANNEL = "welcome"
NICKS=["example1","example2","example3"]
bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    print("bot starrted")

@bot.event

async def on_memeber_join(member):
    welcome_channel = discord.utils.get(member.guild.channels,name=WELCOME_CHANNEL)

