# Knights of the Square Mainfile
# Author: Jesse Cabell
# Licensed under GPL 2.0
# 09/19/2020

import discord

# Quick prototype code
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NzU2ODcwNzUwODc4ODI2NTM1.X2YI0A.CvBFkLTD_dKTJ7pIrUazUg9Lu2w')
