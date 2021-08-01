import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '회륜아 ')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="유격훈련"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def 전역(ctx):
    await ctx.send('51234')

client.run(os.environ['token'])