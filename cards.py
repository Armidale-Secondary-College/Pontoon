import random

def packsort(elem):
    if len(elem) == 3:
        deck, suite, card = elem
    else:
        suite, card = elem
    #print('entered packsort with {0} {1} ' .format (suite ,card))
    cards = {'A':1,'J':11,'Q':12,'K':13}
    suites = {'S':100,'H':200,'D':300,'C':400}
    if card not in cards.keys():
        card = int(card)
    else:
        card = int(cards[card])
    #print(suites[suite] + card)
    return suites[suite] + card

class deck:
    def __init__(self):
        self.debug = True
        pack = []
        if self.debug: print('initiate a deck object')
        for cards in range(1,14):
            for suite in ["S","H","D","C"]:
                if cards == 1:
                    pack.append((suite,'A'))
                elif cards == 11:
                    pack.append((suite,'J'))
                elif cards == 12:
                    pack.append((suite,'Q'))
                elif cards == 13:
                    pack.append((suite,'K'))
                else:
                    pack.append((suite,str(cards)))
        pack.sort(key=packsort)
        self.pack = pack
        self.cardcount = 0
        print(self.pack)
        return
        
    def shuffle(self):
        if self.debug: print('shuffle entered')
        return random.shuffle(self.pack)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.cardcount += 1
        if self.cardcount < len(self.pack):
            width = len(self.pack[self.cardcount])
            card = self.pack[self.cardcount][width-1] + self.pack[self.cardcount][width-2]
            return card
        else:
            raise StopIteration
        
    def __str__(self):
        if self.debug: print('__str__ entered')
        deck_str = ''
        for card in self.pack:
            deck_str += str(card) + '\n'
        if self.debug: print(deck_str)
        return deck_str
        
class shoe(deck):
    def __init__(self, decks=3):
        packs = []
        super().__init__()
        for num in range (0, decks):
            for card in self.pack:
                packs.append((num, card[0], card[1]))
        self.pack=packs
        
 class pontoon()           
                
            