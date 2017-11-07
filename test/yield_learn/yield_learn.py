# -*- coding: utf-8 -*-

from collections import namedtuple

# 使用命名元组，可以简单的构建一个对象
Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    # 2-A
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 4种花色
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        # 构建扑克牌
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        print(self._cards)
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


kk = FrenchDeck()
print(len(kk))
print(kk[1:3])
print(kk.__getitem__(3))