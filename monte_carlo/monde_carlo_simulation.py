import random

class FairRoulette():
    def __init__(self):
        self.pockets = []

        for i in range(1, 37):
            self.pockets.append(i)
        
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1

        self.count_bet = 0
        self.count_not_bet = 0

    def spin(self):
        self.ball = random.choice(self.pockets)
    
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            self.count_bet += 1
            return amt * self.pocketOdds
        
        else:
            self.count_not_bet += 1
            return - amt
    
    def __str__(self):
        return "Fair Roulette"

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append("0")
    
    def __str__(self):
        return "European Roulette"
    
class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append("00")
    
    def __str__(self):
        return "American Roulette"
    
def playRoulette(game, numSpins, pocket, bet, toPrint = False):
    total = 0
    for i in range(numSpins):
        game.spin()
        total += game.betPocket(pocket, bet)

    if toPrint:
        print(numSpins, "spins of", game)
        print("Expected return betting", pocket, "=", \
              str(100 * total / numSpins) + "%")
        print("Bet {} times out of {}\n".format(game.count_bet, game.count_bet + game.count_not_bet))
        game.count_bet = 0
        game.count_not_bet = 0

    return (total / numSpins)

if __name__ == "__main__":
    # game = FairRoulette()
    # game = EuRoulette()
    game = AmRoulette()
    print(len(game.pockets), game.pocketOdds)
    

    for numSpins in (100, 1000, 10000, 100000, 1000000):#, 10000000):
        print("-------- New spins --------")
        for i in range(5):
            playRoulette(game, numSpins, 2, 1, True)
            