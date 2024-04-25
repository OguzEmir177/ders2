import discord
from discord.ext import commands
from bilgiler import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='#', intents=intents)

@client.event
async def on_ready():
    print('Bot hazır')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hoşgeldin-reis")
    if channel:
        await channel.send(f'Hoşgeldin_Reis, {member.mention}!')

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gülegüle-reis")
    if channel:
        await channel.send(f'Güle güle Reis, {member.display_name}!')

client.run(token)
