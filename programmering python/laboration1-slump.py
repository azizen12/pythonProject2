import random
import time

streak = int(0)

def main2():
    print ('Välkommen till gissningspelet!')
    gissningar = 0
    hemligtNummer = random.randint(1, 100)
    while kör:
        gissning = int(input('Gissa på ett tal mellan 0-100: '))
        gissningar += 1
        if hemligtNummer > gissning:
            time.sleep(0.2)
            print('Fel nummer, försök med ett högre tal')
        elif hemligtNummer < gissning:
            time.sleep(0.2)
            print('Fel nummer, försök med ett lägre tal')
        elif hemligtNummer == gissning and gissningar > 7:
            time.sleep(0.2)
            print('Rätt svar men så här många försök borde det inte ta!')
        else:
            time.sleep(0.2)
            global streak
            streak += 1
            print(f'Bra jobbat, du klarade spelet på {gissningar} gissningar! ')
            break

main2()

if streak >= 3:
    print('Du har en grym strategi för att klara spelet!')





