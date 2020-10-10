# KnightsFileManager
from lxml import etree
import os

class KnightsFileManager:
    """
        Manages saving gamestate to disk and other misc file management
        tasks for the bot.
    """

    def GetTokenFromFile():
        """Get the secret bot token from file."""
        token_file = open("./xml/token.xml", "rb")
        tree = etree.parse(token_file)
        root = tree.getroot()
        token_file.close()
        return root.text

    def SaveGameToFile(game_id, FEN):
        """Saves FEN to the game's unique XML file."""
        pass

    def AddToGamelist(user_id1, user_id2, game_id):
        """Add game to gamelist XML file"""
        pass

    def RemoveFromGamelist(game_id):
        """Remove target game from XML file"""
        pass
