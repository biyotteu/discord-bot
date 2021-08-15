import discord
from discord.ext import commands
import os
import time
from datetime import datetime, timedelta

time = datetime(2023,1,27)
client = commands.Bot(command_prefix = '회륜아 ')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="유격훈련"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))

#@client.command(aliases=['대체','대체','대체'])   
@client.command()
async def test(ctx, *args):
    await ctx.send('{}'.format(' '.join(args)))

@client.command(aliases=['D-Day','D-day','d-day','남은날','전역일','복무기간'])
async def 전역(ctx):
    await ctx.send('D-' + str((time-datetime.now()).days))

@client.command()
async def 응애(ctx):
    await ctx.send('응애 나 아가 회륜이><')

@client.command()
async def 코드(ctx):
    stream = os.popen('python test.py')
    await stream.read()

client.run(os.environ['token'])