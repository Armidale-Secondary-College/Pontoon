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
        #print (random.randrange(1,len(self.pack)))
        #for i in range (0,random.randrange(1,len(self.pack))):
            #print (random.randrange(1,len(self.pack)))
        random.shuffle(self.pack)
        return 
        
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
        
class pontoon():       
    def __init__(self, players=1):
        self.players = players
        self.deck = shoe()
        self.deck.shuffle()
        self.handscore = {}
        for player in range(0,self.players):
            self.handscore[player] = 0
        return
                
    def deal(self):
        self.game = {}
        for player in range(0, self.players+1):
            self.game [player] = [self.deck.__next__()]
        for player in range(0, self.players+1):
            self.game [player].append(self.deck.__next__())
            
    def hit(self,player):
        self.game [player].append(self.deck.__next__())
        
    def hand(self, player):
        score = 0
        acelist = []
        for i in self.game[player]:
            if i[0] == 'J': score +=10
            elif i[0] == 'Q': score +=10
            elif i[0] == 'K': score +=10
            elif i[0] == 'A': 
                score += 11
                acelist.append(i)
            else: score += int(i[0])
        for i in acelist:
            if score > 21:
                score -= 10
        self.handscore[player] = score
        return score
    
    def play(self):
        for player in range(1, self.players):
            while self.hand(player) <= 21:
                self.hit(player)
    
    def __str__(self):
        depth = 2
        lines = []
        for player, hand in self.game.items():
            depth = max(depth,len(hand))
        for i in range(0, depth):
            line = ''
            for player, hand in self.game.items():
                if i <= len(hand):
                    line += str(hand[i-1])
                line += '\t'
            lines.append(line)
        line = 'Dealer\t'
        for i in range(0, self.players):
            line += 'Player' + str(i+1) + '\t'
        lines.append(line)
        print(lines)
        lineout = ''
        for line in lines:
            lineout += line +'\n'
        return lineout
            
            