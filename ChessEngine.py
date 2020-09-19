# ChessEngine.py
# Use to manage the boardstate of a game of chess using PGN and FEN data.
# Output a PNG of the boardstate to be used as seen fit.
# Designed to be used with a messaging system as a bot core.
# Author: Jesse Cabell
# Licensed Under GPL 3.0
# 09/19/2020

import io
from lxml import etree

class ChessEngine:
    # Vars
    FEN = ""
    PGN = ""
    UserID1 = "" # User1 is always white
    UserID2 = "" # User2 is always black
    GameID = ""

    def __init__(self, FEN="", PGN="", UserID1="", UserID2="", GameID=""):
        self.FEN=FEN
        self.PGN=PGN
        self.UserID1=UserID1
        self.UserID2=UserID2
        self.GameID=GameID

    def SetBoardFromFEN():
        # Process the given FEN and load boardstate into memory
        pass

    def NewGame():
        # Set up a new FEN, generate Game ID, save to game list, and save to file.
        SetBoardFromFEN('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        GenerateGameID()
        AddToGamelist()

    def EndGame():
        # Update game list, stats, and delete game data file from drive.
        RemoveFromGameList()
        UpdateStats()

    def ExportBoardImage():
        # First generate SVG, and then convert to PNG using Inkscape
        pass

    def SaveGameToFile():
        # Save the PGN and FEN to (gameid).xml
        # game_file = open('./xml/'+self.GameID+'.xml', 'wa')
        pass

    def CheckMove():
        # Run algorithm to see if a move is possible.
        # If yes, leave blank.
        # If no, return 'invalid'
        pass

    def MakeMove():
        # Update PGN and FEN with new data.
        # If, after the FEN is updated, a player is in check, return a status
        # of 'check'. If the player is in checkmate, return 'checkmatew' or
        # 'checkmateb'. Otherwise, return blank. If the game hits checkmate,
        # run EndGame.
        pass

    def GenerateGameID():
        # Use both userids and the current time to generate a game hash
        pass

    def AddToGameList():
        # Create game list file if it doesn't exist, then append this game to the list.
        pass

    def RemoveFromGameList():
        # Find this game in the game list, and remove it
        pass

    def UpdateStats():
        # Update the stat list with the appropriate w/d/l stats for each player.
        pass
