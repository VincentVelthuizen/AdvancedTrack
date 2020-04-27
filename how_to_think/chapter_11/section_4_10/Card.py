class Card:
    """
    Represents a playing card

    Spades --> 3
    Hearts --> 2
    Diamonds --> 1
    Clubs --> 0

    Jack --> 11
    Queen --> 12
    King --> 13
    """

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.ranks[self.rank], self.suits[self.suit])

    def cmp(self, other):
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1

        if self.rank == other.rank:
            return 0
        if (self.rank > other.rank or self.rank == 1) and other.rank != 1:
            return 1

        return -1

        # the cards are the same
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0