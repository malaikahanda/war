import random
from datetime import datetime

# How many cards per suit? Standard is 13.
N_CARDS = 13

# How many suits? Standard is 4. MUST BE EVEN.
N_SUITS = 4

# Represent faces + Ace as numbers, since nothing matters.
DECK = [i for i in range(N_CARDS) for j in range(N_SUITS)]

# Storing the data.
DATE = datetime.today().strftime("%Y-%m-%d")
HISTORY_PATH = "data/history.csv"
GAME_DATA_PATH = "data/past_games/" + DATE + ".csv"
MOST_RECENT_GAME_PATH = "data/most_recent_game.csv"
DATA = ["round,player,cards"]


def play_round(p1, p2, cards):

    # Play the first card 
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)

    # Someone wins the round:
    if p1_card > p2_card:
        all_cards = cards + [p1_card, p2_card]
        random.shuffle(all_cards)
        p1.extend(all_cards)
        return p1, p2
    elif p2_card > p1_card:
        all_cards = cards + [p1_card, p2_card]
        random.shuffle(all_cards)
        p2.extend(all_cards)
        return p1, p2

    # Or, we go to war:
    else:
        cards.append(p1_card)
        cards.append(p2_card)
        return go_to_war(p1, p2, cards)


def go_to_war(p1, p2, cards):

    # Deal three cards, but only if the players have enough.
    for i in range(3):
        if len(p1) == 0:
            random.shuffle(cards)
            return p1, p2 + cards
        elif len(p2) == 0:
            random.shuffle(cards)
            return p1 + cards, p2
        else:
            cards.append(p1.pop(0))
            cards.append(p2.pop(0))

    if len(p1) == 0:
        random.shuffle(cards)
        return p1, p2 + cards
    elif len(p2) == 0:
        random.shuffle(cards)
        return p1 + cards, p2
    else:
        return play_round(p1, p2, cards)


if __name__ == "__main__":

    # Shuffle the deck.
    random.shuffle(DECK)

    # Deal the cards.
    half = len(DECK) // 2
    p1, p2 = DECK[: half], DECK[half :]

    # Count the rounds.
    rounds = 1

    # Main game loop
    while True:

        DATA.append("{},{},{}".format(rounds, "p1", len(p1)))
        DATA.append("{},{},{}".format(rounds, "p2", len(p2)))

        # Play for as long as both players have cards.
        if len(p1) == 0:
            win_text = "Player 2"
            break
        elif len(p2) == 0:
            win_text = "Player 1"
            break
        elif rounds > 1000:
            win_text = "Infinite Game"
            break

        p1, p2, = play_round(p1, p2, cards=[])
        rounds += 1

    # Save the data
    lines = "\n".join(DATA)
    with open(GAME_DATA_PATH, "w") as f:
        f.write(lines)
    with open(MOST_RECENT_GAME_PATH, "w") as f:
        f.write(lines)
    with open(HISTORY_PATH, "a") as f:
        f.write("\n{},{},{}".format(DATE, win_text, rounds))

