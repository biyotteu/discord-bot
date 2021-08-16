import discord
from discord.ext import commands
import os
from datetime import datetime, timedelta
import requests
import youtube_dl

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
async def test(ctx, *,context):
    await ctx.send(context)

@client.command(aliases=['D-Day','D-day','d-day','남은날','전역일','복무기간'])
async def 전역(ctx):
    await ctx.send('D-' + str((time-datetime.now()).days))

@client.command()
async def 응애(ctx):
    await ctx.send('응애 나 아가 회륜이><')

@client.command()
async def req(ctx,url):
    con = requests.get(url).text
    idx = 0
    size = len(con)
    limit = 2000
    while True:
        if idx > size:
            break
        await ctx.send(con[idx:min(size,idx+limit)])
        idx = idx + limit
    await ctx.send()

@client.command()
async def python(ctx,*,code):
    f = open("test.py","w")
    f.write(code)
    f.close()
    stream = os.popen('python test.py')
    await ctx.send(stream.read())

@client.command(pass_context = True)
async def 이리온(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("통화방에 없자너 이자슥아")

@client.command()
async def 나가(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("빠이염")

@client.command()
async def id(ctx):
    await ctx.send(ctx.message.author.id)

@client.command()
async def 니가너무좋아(ctx):
    if ctx.message.author.id != '342314679881826322':
        await ctx.send("넌 안돼^^")
        return
    
    if (ctx.author.voice):
        voiceChannel = ctx.message.author.voice.channel
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio("KakaoTalk_20210816_222050455.mp3"))

@client.command()
async def 노래불러줘(ctx,url):
    is_song = os.path.isfile("song.mp3")
    try:
        if is_song:
            os.remove("song.mp3")
    except:
        pass

    if (ctx.author.voice):
        voiceChannel = ctx.message.author.voice.channel
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
# @client.command()
# async def pip(ctx,context):
#     stream = os.popen('pip install '+context)
#     await ctx.send(stream.read())

client.run(os.environ['token'])