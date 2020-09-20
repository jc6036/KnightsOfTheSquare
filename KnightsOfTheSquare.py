# Knights of the Square Mainfile
# Author: Jesse Cabell
# Licensed under GPL 3.0
# 09/19/2020
##############################
# KnightsOfTheSquare.py
#
# This file manages communication with the Discord API.
# It takes API events, transports them to the chess engine backend,
# and transports the responses back to the Discord API.


import discord
import io
import os
from lxml import etree
import chess

# Setup param vars that can be changed with commands later
####################
delimiter = '$'
help_msg = \
"""
$challenge (User ID) (First Move) - Use this to start a match with someone. Keep track of the Game ID!
$move (Game ID) (notation) - Make a move if it's your turn.
$takeback (Game ID) (move number) - Reverse the game to the given move number. The other player must accept.
$resign (Game ID) - Give up! The game will be recorded as a loss for you, and a win for your opponent.
$draw (Game ID) - Propose a draw. The other player must accept to draw the game.
$board (Game ID) - Get an image of the board and the last 5 moves made.
$games (User ID) - Get a list of games this user is currently in.
$ratio (User ID) - Gives the W/D/L ratio for the given user, in white and black.
$moves (Game ID) - Gives a list of the moves in the game so far.
$settings (setting name) (setting change) - Just use settings to see a list. Then you can change settings such as delimiter.

Moves are in Standard Algebraic Notation. The basic structure of a SAN move is
<piece><target square>.

Some examples:
Ne4 - Move a knight to e4, if there is only one knight that can move there.
Nce4 - Move the knight on the C file to e4
Qe1 - Move the queen to e1
Qh4e1 - Move the queen on h4 to e1
Rxh8 - Rook captures h8.
Kd4 - King to d4
O-O - Kingside Castle
O-O-O - Queenside Castle
e8=Q - Promote pawn to queen

If you're having trouble, google Standard Algebraic Notation and find a tutorial.
"""

# Function Defs
####################
def GetTokenFromFile():
    token_file = open("./xml/token.xml", "rb")
    tree = etree.parse(token_file)
    root = tree.getroot()
    token_file.close()
    return root.text

def GenerateBoardImage(board, game_id):
    # Use syscall to pipe our chess SVG into Inkscape, and convert to PNG
    boardsvg = chess.svg.board(board=board)
    file = open(game_id+'.svg', "w")
    file.write(boardsvg)
    file.close()
    subprocess.call(['inkscape', '--export-type=png', game_id+'.svg'])

def GenerateGameID(user_id1, user_id2):
    return "testid"

def UpdateGameList(user_id1, user_id2, game_id):
    pass

def SaveGameToFile(game_id, FEN):
    # Save FEN to game file.
    pass

def EmbedBoardImage(embed, board, game_id):
    # embed is a discord.Embed object. This func returns it, after adding image.
    # board is the chessboard object, used to generate the image.
    GenerateBoardImage(board, game_id)
    file = discord.File('./xml/'+game_id+'.png',game_id+'.png') # Path, and Filename
    embed.set_image(url='attachment://'+game_id+'.png')
    return embed

def CleanupBoardImage(game_id):
    os.remove('./xml/'+game_id+'.png')
    os.remove('./xml/'+game_id+'.svg')

# Main Code
####################
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Make sure the message we are seeing isn't coming from us
    if message.author == client.user:
        return

    # Command one: challenge. Start a new game; checks validity of
    # given user id, then checks possibilty of first move before
    # saving to file.
    if message.content[0] == delimiter:
        if message.content.startswith(delimiter+'challenge'):
            command_list = message.content.split()
            if client.get_user(command_list[1]) == None:
                await message.channel.send('That does not appear to be a valid user. Try again.')
                return
            else:
                user_id1 = message.Author
                user_id2 = command_list[1]
                move = command_list[2]
                board = chess.Board()
                if board.parse_san(move) in board.legal_moves == True:
                    board.push_san(move)
                    game_id = GenerateGameID(user_id1, user_id2)
                    UpdateGameList(user_id1, user_id2, game_id)
                    SaveGameToFile(game_id,board.fen(),1)
                    GenerateBoardImage(board, game_id)
                    embed = discord.Embed()
                    EmbedBoardImage(embed, board, game_id)
                    embed.title = 'Game on!'
                    await message.channel.send(content='Your turn, @'+user_id2, file=file, embed=embed)
                    CleanupBoardImage(game_id)
                else:
                    await message.channel.send('That move is invalid. Challenge aborted.')

        # Help command. Displays contents of help message.
        # Also includes some hints on Standard Algebraic Notation.
        elif message.content.startswith(delimiter+'help'):
            embed = discord.Embed()
            embed.title = "Did anybody need my commands?"
            embed.description = help_msg
            await message.channel.send(embed=embed)

        # Used to make a clean exit for testing purposes.
        # Will be removed upon completion.
        elif message.content.startswith(delimiter+'quit'):
            await message.channel.send('Shutting down. See ya!')
            await client.close()

        else:
            await message.channel.send('Sorry, that command is not recognized. Use $help to see my commands.')

client.run(GetTokenFromFile())
