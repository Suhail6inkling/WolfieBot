import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
import os
from os import listdir
from os.path import isfile, join
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from cogs.lib.roles import *
from cogs.lib.variables import *

try:
    from config import TOKEN
except ModuleNotFoundError:
    TOKEN = os.environ['TOKEN']

client = commands.Bot(command_prefix=("W.","w."))

game_channel = client.get_channel(392995027909083137)
voting_channel = client.get_channel(480455087869919244)
notes_channel = client.get_channel(393476547954212874)
dead_channel = client.get_channel(392995124423950344)


global Day, PlayerInfo, Actions, Attacks
Day = False
DayCount = 0
PlayerInfo = []
Actions = []
Attacks = []

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity=discord.Game(name="Say w.help"))
    chan = client.get_channel(392995207894925313)
    await chan.send("WolfieBot online!")

client.remove_command("help")


if __name__ == "__main__":
    for extension in [f.replace('.py', '') for f in listdir("cogs") if (isfile(join(cogs_dir, f)) and f.endswith(".py"))]:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.run(TOKEN)
