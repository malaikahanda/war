## This is a twitter bot that documents the War rivalry of two imaginary players

Twitter handle:

Each day, the following things happen:

1. `play_war.py` is executed:
    - A simulated game of War is played out between two players
    - In order to avoid infinite games, the script injects a bit of randomness: when each player adds cards back to their deck, the newly acquired cards are shuffled first
    - The flow of cards during the rounds is stored in`data/most_recent_game.csv`
    - The winner, date, and total number of rounds are stored in `data/history.csv`
2. `make_line_graph.R` is executed:
    - The line graph displays data from `most_recent_game.csv` to show the card movement throughout the game
    - The graph is saved as a 4x6 png
3. `make_histogram.R` is executed:
    - The histogram displays data from `history.csv1`, showing the distribution of the number of rounds in a game
    - The graph is saved as a 4x6 png
4. `make_pct_graph.R` is executed:
    - This graph shows the percentage of games that each player has won over time
    - The graph is saved as a 4x6 png
4. `send_tweet.py` is executed.
    - Text is formatted to show who won the game, how many rounds it took, how many games they have won, and the average number of rounds in a game
    - The text is sent as a tweet, with the three graphs attached