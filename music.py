import discord
from discord.ext import commands
import lavalink
from discord import utils
from discord import Embed, player
import random


class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('localhost', 6969, 'test', 'eu', 'music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    @commands.command(name='join')
    async def join(self, ctx):
        member = utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
        if member is not None and member.voice is not None:
            message = await ctx.send('joining...')
            message
            vc = member.voice.channel
            player = self.bot.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
            if not player.is_connected:
                player.store('channel', ctx.channel.id)
                await self.connect_to(ctx.guild.id, str(vc.id))
            await message.edit(content=f'joined ***{vc}***')

    @commands.command(name="leave")
    async def leave(self, ctx):
        message = await ctx.send("leaving...")
        message
        vc = await self.connect_to(ctx.guild.id, None)
        vc
        messageone = "why are you forcing me to leave bro?"
        messagetwo = "that's not very gangster bro"
        rand = (messageone, messagetwo)[random.randint(0, 1)]
        await message.edit(content=f'i have left ***{"Algemeen"}***  but ' + rand)


    @commands.command(name='play')
    async def play(self, ctx, *, query):
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            query = f'ytsearch:{query}'
            results = await player.node.get_tracks(query)
            tracks = results['tracks'][0:10]
            i = 0
            query_result = ''
            for track in tracks:
                i = i + 1
                query_result = query_result + f'{i}) {track["info"]["title"]} - {track["info"]["uri"]}\n'
            embed = Embed()
            embed.description = query_result

            await ctx.channel.send(embed=embed)

            def check(m):
                return m.author.id == ctx.author.id

            response = await self.bot.wait_for('message', check=check)
            track = tracks[int(response.content)-1]

            player.add(requester=ctx.author.id, track=track)
            if not player.is_playing:
                await player.play()

        except Exception as error:
            print(error)

    @commands.command(name="pause")
    async def pause(self, ctx):
        message =await ctx.send("pausing...")
        message
        player = self.bot.music.player_manager.get(ctx.guild.id)
        await player.set_pause(True)
        await message.edit(content="paused")

    @commands.command(name="resume")
    async def resume(self, ctx):
        message = await ctx.send("resuming...")
        message
        player = self.bot.music.player_manager.get(ctx.guild.id)
        await player.set_pause(False)
        await message.edit(content="resumed")

    @commands.command(name="skip")
    async def skip(self, ctx):
        message = await ctx.send("skipping song...")
        player = self.bot.music.player_manager.get(ctx.guild.id)
        await player.skip()
        await message.edit(content="skipped.")


def setup(bot):
    bot.add_cog(MusicCog(bot))
