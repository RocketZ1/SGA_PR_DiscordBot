import discord
from discord.ext import commands

# Set up bot prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# Event for bot being ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


RSOChannels = {}


def addRSOChannel(rso_id: int, channel_id: int) -> None:
    if rso_id in RSOChannels:
        if channel_id in RSOChannels[rso_id]:
            return
        BC_Channels = RSOChannels[rso_id]
        BC_Channels.append(channel_id)
        RSOChannels[rso_id] = BC_Channels
    else:
        BC_Channels = [channel_id]
        RSOChannels[rso_id] = BC_Channels


def getRSOName(rso_id: int) -> str:
    print(RSOChannels)
    return "TempName"


# Command to send a message in a text channel
@bot.command()
async def set_rso(ctx, rso_id: int):
    channel = ctx.message.channel
    if channel:
        addRSOChannel(rso_id, channel.id)
        await channel.send("RSO channel added successfully for " + getRSOName(rso_id))
    else:
        await ctx.send("RSO ID not found, please try again!")


tokenFile = open("token.txt", "r")
token = tokenFile.read()

# FL Polytechnic SGA PR Bot token
bot.run(token)
