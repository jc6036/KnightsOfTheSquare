This directory is used to store data while the bot is running.

Files:
(Game ID).xml - Stores FEN and PGN for a single game.
games.xml - Stores list of games with user IDs participating in game
stats.xml - Stores stats about each User ID
token.xml - This file is NOT uploaded to github. If you are forking this bot,
            you will want to create this XML file and add your bots token to it.
            <token>(token)</token> should be sufficient. The other XML files
            will be created automatically if they do not exist. If this file
            does not exist, you will receive a warning when you try to run
            the bot. I am leaving it as a manual creation as a security feature
            for your bot. The .gitignore is also configured to ignore XML files.
