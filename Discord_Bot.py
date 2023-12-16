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
    await welcome_channel.send(f"welcome {member.mention}, please read our rules and have a great time!")

@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx,user:discord.Member):
    await ctx.guild.ban(user,delete_message_days=0)
    await ctx.send(f"banned {user}")


@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx,user:discord.User):
    await ctx.guild.unban(user)
    await ctx.send(f"unbanned {user}")


@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx,user:discord.User):
    await ctx.guild.kick(user)
    await ctx.send(f"kicked {user}")

@bot.command(aliases=["rnick"])
async def random_nick(ctx):
    new_nick = random.choice(NICKS)
    await ctx.author.edit(nick=new_nick)
    await ctx.send(f"Your new nickname is {new_nick}")


@commands.has_permissions(manage_nicknames=True)
@bot.command(aliases=["change_name"])
async def change_nick(ctx,user:discord.Member,*,new_nick):
    await user.edit(nick=new_nick)
    await ctx.send(f"Change the nick of {user.mention} to `{new_nick}`")

