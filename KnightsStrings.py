class KnightsStrings:
    """Functions as a string table for the bot."""

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
