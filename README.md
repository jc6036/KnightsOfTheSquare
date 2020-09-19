# KnightsOfTheSquare
A chess bot for discord. Play games with other members of your server using chess notation.

Use this link to add the bot to your server<br>
https://discord.com/api/oauth2/authorize?client_id=756870750878826535&permissions=93248&scope=bot

Commands:
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

All moves are in standard algebraic notation. Please see this link:<br>
https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
