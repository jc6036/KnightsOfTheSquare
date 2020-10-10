# Knights of the Square - Play chess with your friends on discord!
# Author: Jesse Cabell
# Licensed under GPL 3.0
# 09/19/2020
##############################
import discord
import io
import chess
import KnightsFileManager
import KnightsDebug
import KnightsStrings

class KnightsOfTheSquare:
    """
        Ties together the chess engine, file management service, and discord.py
        event management.
    """

    def __init__(self):
        self.client = discord.Client()
        self.delimiter = '$'
        self.help_msg = KnightsStrings.help_msg
        self.user_id1 = ""
        self.user_id2 = ""
        self.game_id = ""
        self.FEN = ""
        self.board = chess.Board()

    def start():
        """Starts the bot client"""
        manager = KnightsFileManager()
        client.run(manager.GetTokenFromFile())

    def GenerateGameID(user_id1, user_id2):
        return "testid"

    async def SendSimpleMessage(messagetxt, title):
        """Send simple embed message with a title and body."""
        embed = discord.Embed()
        embed.title = title
        embed.description = messagetxt
        await message.channel.send(embed=embed)

    async def Shutdown():
        """Cleanly shuts down the bot for testing purposes."""
        await message.channel.send('Shutting down. See ya!')
        await client.close()

    @client.event
    async def on_ready():
        """When the client is logged in and ready for new events, this fires."""

        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        """
            When a message is sent to the server, this fires. Message object
            is passed through to this event handler.

            This method parses the message and calls the appropriate method to
            process it.
        """

        # Make sure the message we are seeing isn't coming from us
        if message.author == client.user:
            return

        # $challenge - primary command to start a game
        if message.content[0] == delimiter:
            
            if message.content.startswith(delimiter+'challenge'):
                command_list = message.content.split()
                if client.get_user(command_list[1]) == None: #TODO: Why the fuck does this not work?
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

            # $help - display help message in a nice looking embed.
            elif message.content.startswith(delimiter+'help'):
                await SendSimpleMessage(KnightsStrings.help_msg, "Did anybody need my commands?")

            # $quit - debug command, shuts down bot cleanly for faster testing.
            elif message.content.startswith(delimiter+'quit'):
                await Shutdown()

            else:
                await message.channel.send('Sorry, that command is not recognized. Use $help to see my commands.')
