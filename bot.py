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
    client.load_extension('cogs.music')
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

    De een en alleen gangster#0733 (Reason : Make)

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








client.run(token)
