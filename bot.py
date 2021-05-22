import discord
from discord.ext import commands
import time
import asyncio
import os
import playsound
from ffmpeg import FFmpeg

client = commands.Bot(command_prefix = '<')
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

client.remove_command('help')
@client.command(pass_context=True)
async def h(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='<ping', value='Returns bot respond time in milliseconds', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def play(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.author.voice.channel
    if channel:
        print(channel.id)
    await channel.connect()
    guild = ctx.guild
    audio_source = discord.FFmpegPCMAudio('/home/julij/BOTdiscord/Minecraft.mp3')
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
    elif contents.startswith("volume"):
            volume = contents
            volume = volume.strip("volume ")
            volume = int(volume)

            if volume <= 200:
                volume = volume / 10
                vc.source = discord.PCMVolumeTransformer(vc.source)
                vc.source.volume = volume
            else:
                message.channel.send("Please give me a number between 0 and 100!")

client.run('ODQ1MjU2NTY3NzQwNjk0NTM4.YKeUhQ.M_Fzl4qXy3NpC2oWT12Gisf6fzE')
