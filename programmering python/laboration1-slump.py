import random
from operator import truediv


hemligtNummer = random.randint(1, 100)

def main2():
    print ('Välkommen till gissningspelet!')
    gissningar = 1
    while True:
        gissning = int(input('Gissa på ett tal mellan 0-100: '))
        gissningar += 1
        if hemligtNummer > gissning:
            print('Fel nummer, försök med ett högre tal')
        elif hemligtNummer < gissning:
            print('Fel nummer, försök med ett lägre tal')
        else:
            print(f'Bra jobbat, du klarade spelet på {gissningar} gissningar! ')






main2()