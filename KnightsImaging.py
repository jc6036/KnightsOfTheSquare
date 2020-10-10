import chess
import discord.py

class KnightsImaging:
    """Handles chessboard image generation and management."""

    def __init__(self, game_id, board, embed):
        """
            game_id: unique ID for game in question
            board: board object from chess library
            embed: discord embed object to add image to

            All 3 params are required for complete functionality.
        """
        self.game_id = game_id
        self.board = board
        self.embed = embed
        self.svg_filename = self.game_id+'.svg'
        self.png_filename = self.game_id+'.png'

    def GenerateBoardImage():
        """Generate a SVG of the boardstate."""
        boardsvg = chess.svg.board(board=self.board)
        file = open(self.svg_filename, "w")
        file.write(boardsvg)
        file.close()

    def ConvertSVGtoPNG():
        """Pipe the SVG to inkscape via command line, export as PNG."""
        subprocess.call(['inkscape', '--export-type=png', self.svg_filename])

    def EmbedBoardImage():
        """Add discord file object into a discord embed object for presentation."""
        file = discord.File('./xml/'+self.png_filename, self.png_filename) # Path, and Filename
        self.embed.set_image(url='attachment://'+self.game_id+'.png')

    def CleanupBoardImage():
        """File cleanup for board images."""
        os.remove('./xml/'+self.png_filename)
        os.remove('./xml/'+self.svg_filename)
