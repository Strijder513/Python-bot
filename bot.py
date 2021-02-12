import discord
from discord.ext import commands
import random
import youtube_dl
import os
import datetime
import time
from datetime import datetime


client = commands.Bot(command_prefix='.')
game = discord.Game("een gangster voor mijn neger zijn")
black = 0x000000
token = ''




@client.event
async def on_ready():
    print("------------")
    print("on")
    print('------------')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)
    global startdate
    startdate = datetime.now()


@client.command()
async def website(ctx):
    embed1 = discord.Embed(title="website",
                           url="https://thegangster.site", description="best website known to mankind", color=0xFF5733)
    embed1.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed1.set_thumbnail(url="https://imgur.com/kJvgh4s.jpeg")
    await ctx.send(embed=embed1)


@client.command()
async def embed(ctx):
    embed2 = discord.Embed(title="embeds you can use",
                           description="""



    .website
    .helpers

    """, color=0xFF5733)
    embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed2)




@client.command()
async def uptime(ctx):
    now = datetime.now()
    uptime = now - startdate
    await ctx.send(f'```{uptime}```')


@client.command()
async def helpers(ctx):
    embed3 = discord.Embed(title="helpers",

                           description="""

    Helpers

    De een en alleen gangster#0733 (Reason : Maker)

    kais dad#5789 

    GANGSTER#6680 
    """, colour=black)
    embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed3.set_thumbnail(url="https://i.imgur.com/r3OtRxy.jpg")
    await ctx.send(embed=embed3)


@client.command()
async def latency(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')


@client.event
async def on_command_error(ctx1, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx1.send('you need the requirements homes https://tenor.com/view/homes-cholo-swag-kid-cool-gif-14704703')
    if isinstance(error, commands.MissingPermissions):
        await ctx1.send('no permissions homes https://tenor.com/view/homes-cholo-swag-kid-cool-gif-14704703')



@client.command()
async def ping(ctx):
    await ctx.send("nigga")


@client.command()
async def clear(ctx, amount=10, ):
    await ctx.send("purging messages please wait...")
    time.sleep(1.5)
    await ctx.channel.purge(limit=amount + 1)
    time.sleep(1.0)
    await ctx.send(f'done purging **{amount}** messages')


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'kicked {member.mention}')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')



@client.command()
async def join(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Algemeen')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect()
    await ctx.send(f'ready to play music on ***{voiceChannel}***')


@client.command()
async def play(ctx, url: str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await ctx.send("I'M NOT IN THE FUCKING CALL")
    else:
        await ctx.send("playing song...")
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Song playing, stop it or listen to it")
            return

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
        return


@client.command()
async def p(ctx, url: str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await ctx.send("I'M NOT IN THE FUCKING CALL")
    else:
        await ctx.send("playing song...")
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Song playing, stop it or listen to it")
            return

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
        return


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()
    messageone = "why are you forcing me to leave bro?"
    messagetwo = "that's not very gangster bro"
    rand = (messageone, messagetwo)[random.randint(0, 1)]
    await ctx.send(rand)


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send("pausing...")
    await voice.pause()


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send("resuming...")
    await voice.resume()


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send("stopping...")
    await voice.stop()


client.run(token)
