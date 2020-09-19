import csv
import tokens
import tweepy

# Formatting.
PLAYERS = {"p1": "Player 1", "p2": "Player 2"}


# Reading the data.
HISTORY_PATH = "data/history.csv"
GAME_PATH = "data/most_recent_game.csv"
IMAGE_PATHS = ["data/most_recent_line.png",
               "data/most_recent_pct.png",
               "data/most_recent_hist.png"]


# I know that I could use pandas but I simply do not want to :)


def parse_game():
    with open(GAME_PATH) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["cards"]) == 52:
                return row["player"], int(row["round"])
    return None, None


def parse_history(winner) :
    num, denom, total_wins = 0, 0, 0
    with open(HISTORY_PATH) as f:
        reader = csv.DictReader(f)
        for row in reader:
            num += int(row["rounds"])
            denom += 1
            if row["winner"] == PLAYERS[winner]:
                total_wins += 1
    return num, denom, total_wins

def write_tweet():
    winner, n_rounds = parse_game()
    num, denom, total_wins = parse_history(winner)
    
    tweet = "{} won today's game after {} rounds!".format(PLAYERS[winner], n_rounds)
    tweet += "\n{} has won {} of {} total games.".format(PLAYERS[winner], total_wins, denom)
    tweet += "\n\nThe average length of a game is {} rounds.".format(round(num / denom))
    return tweet


if __name__ == "__main__":
    
    # Set up the authentication.
    auth = tweepy.OAuthHandler(tokens.API_KEY, tokens.API_KEY_SECRET) 
    auth.set_access_token(tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Upload multiple images.
    media_ids = []
    for filename in IMAGE_PATHS:
        res = api.media_upload(filename)
        media_ids.append(res.media_id)

    # Tweet with multiple images
    tweet_text = write_tweet()
    print(tweet_text)
    api.update_status(status=tweet_text, media_ids=media_ids)

