import random
class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank] , Card.suit_names[self.suit])

    def __lt__(self, other):
        '''
        卡牌比较，优先花色
        :param other:
        :return:

        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.rank < other.rank
        '''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        '''
        移出牌
        :return:
        '''
        return self.cards.pop()

    def add_card(self,card):
        return self.cards.append(card)

    def shuffle(self):
        '''
        打乱顺序
        :return:
        '''
        random.shuffle(self.cards)
        return self

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label



c1 = Card(1, 12)
c2 = Card(2, 11)
print(c1 < c2)
deck = Deck()
print("正序：\n", deck)
print("乱序：\n",deck.shuffle())
