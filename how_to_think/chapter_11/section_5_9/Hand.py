from how_to_think.chapter_11.section_4_10.Deck import Deck


class Hand(Deck):

    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

    def add(self, card):
        self.cards.append(card)
