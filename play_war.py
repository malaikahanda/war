import random

# How many cards per suit? Standard is 13.
N_CARDS = 13

# How many suits? Standard is 4. MUST BE EVEN.
N_SUITS = 4

# Represent faces + Ace as numbers, since nothing matters
DECK = [i for i in range(N_CARDS) for j in range(N_SUITS)]


def play_round(p1, p2, cards):
    print("")

    # Play the first card 
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)

    # Someone wins the round:
    if p1_card > p2_card:
        p1.extend(cards)
        p1.append(p1_card)
        p1.append(p2_card)
        print("P1's {} beats P2's {}".format(p1_card, p2_card))
        print("P1 has {} cards | P2 has {} cards".format(len(p1), len(p2)))
        return p1, p2
    elif p2_card > p1_card:
        p2.extend(cards)
        p2.append(p1_card)
        p2.append(p2_card)
        print("P2's {} beats P1's {}".format(p2_card, p1_card))
        print("P1 has {} cards | P2 has {} cards".format(len(p1), len(p2)))
        return p1, p2

    # Or, we go to war:
    else:
        print("Tie! Both played a {}".format(p1_card))
        print("Going to war...")
        cards.append(p1_card)
        cards.append(p2_card)
        return go_to_war(p1, p2, cards)


def go_to_war(p1, p2, cards):

    # Deal three cards, but only if the players have enough.
    for i in range(3):
        if len(p1) == 0:
            return p1, p2
        elif len(p2) == 0:
            return p1, p2
        else:
            print("DEAL FACEDOWN {}".format(i+1))
            cards.append(p1.pop(0))
            cards.append(p2.pop(0))

    return play_round(p1, p2, cards)


if __name__ == "__main__":

    # Shuffle the deck.
    random.shuffle(DECK)

    # Deal the cards.
    half = len(DECK) // 2
    p1, p2 = DECK[: half], DECK[half :]

    # Count the rounds, so we can show how much time is wasted by this useless
    # idiotic game.
    rounds = 0

    # Play for as long as both players have cards.
    while True:
        if len(p1) == 0:
            print("Player 2 wins!")
            print("Game over after {} rounds".format(rounds))
            break
        if len(p2) == 0:
            print("Player 1 wins!")
            print("Game over after {} rounds".format(rounds))
            break
        p1, p2 = play_round(p1, p2, cards=[])
        rounds += 1


        if rounds > 1000:
            print("TAKING TOO LONG, exit early.")
            break
