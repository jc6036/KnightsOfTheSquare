# Knights of the Square Mainfile
# Author: Jesse Cabell
# Licensed under GPL 2.0
# 09/19/2020
##############################
# KnightsOfTheSquare.py
#
# This file manages communication with the Discord API.
# It takes API events, transports them to the chess engine backend,
# and transports the responses back to the Discord API.


import discord
import io
from lxml import etree

# Setup param vars that can be changed with commands later
####################
delimiter = '$'

# Function Defs
####################
def GetTokenFromFile():
    token_file = open("./xml/token.xml", "rb")
    tree = etree.parse(token_file)
    root = tree.getroot()
    token_file.close()
    return root.text


# client = our main interface with the entire API thanks to discord.py
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

    if message.content.startswith('$quit'):
        await client.Close()

client.run(GetTokenFromFile())
