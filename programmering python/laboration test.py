import random
import time

                #funktion för menyn
def get_menu_option():
    menu_options = ('1', '2', '3', '4')

    while True:
        print()
        print('** MENU **')
        print('1 = Credits')
        print('2 = Tärningar')
        print('3 = Slumpade värden')
        print('4 = Exit')

        print()
        user_input = input(' Välj ett alternativ: ')
        print()

        if user_input in menu_options:
         return user_input

        else:
         print()
         print('OPTION NOT AVAILABLE')

def roll_dice():    #Simulering av 2st tärningskast
    return random.randint(2, 12)

                    #funktion för tärningsspelet
def main():
    print("Välkommen till tärningsspelet!")

    rundor = int(input("Skriv in antalet rundor du vill spela: "))

    spelarPoäng = 0     #Vad varje spelare börjar med
    aiPoäng = 0
    spelarKasten = []    #Listan där varje spelares kast kommer sparas
    aiKasten = []

    for antalRundor in range(1, rundor + 1):    #börjar på runda 1, därav +1 i tak)
        input(f"\n>> Runda {antalRundor} <<\nTryck Enter för att slå tärningen...")

        print('\nSlår kast...\n')
        time.sleep(0.5)


        # Spelarens tur
        spelarKast = roll_dice()            #spelar gör ett kast, åkallar funktionen roll_dice
        spelarKasten.append(spelarKast)     #.append gör att varje kast kommer att läggas till i listan spelarKasten
        print(f"Du slog: {spelarKast}")

        # AI:s tur
        aiKast = roll_dice()
        aiKasten.append(aiKast)
        print(f"AI:n slog: {aiKast}")

                                            #Avgörandet om vem som vinner rundan
        if spelarKast > aiKast:
            print("Du vann denna rundan!")
            spelarPoäng += 1
        elif spelarKast < aiKast:
            print("AI:n vann denna rundan!")
            aiPoäng += 1
        else:
            print("Det blev lika!")

        print(f"Nuvarande poängställning - Du: {spelarPoäng}, AI: {aiPoäng}")

    time.sleep(1)
    print('\n Beräknar resultat..')
    time.sleep(2)

                                            #Avgörandet om vem som vinner
    print("\n-- Matchen är över --")
    print(f"Slutgiltig poängställning - Du: {spelarPoäng}, AI: {aiPoäng}")

    if spelarPoäng > aiPoäng:
        print("Grattis, du vann matchen!!")
    elif spelarPoäng < aiPoäng:
        print("AI:n vann matchen!")
    else:
        print("Matchen blev lika!")
                                            #Beräkning av slutresultat
    totalaSpelarPoäng = sum(spelarKasten)
    totalaAiPoäng = sum(aiKasten)
    medelvärdeSpelare = totalaSpelarPoäng/rundor
    medelvärdeAi = totalaAiPoäng/rundor
    highest_roll = max(spelarKasten + aiKasten)
    lowest_roll = min(spelarKasten + aiKasten)

    print()
    print()
    print(f'Ditt medelvärde av alla kast: {medelvärdeSpelare:.1f}')
    print(f'AI:ns medelvärde av alla kast: {medelvärdeAi:.1f}')
    print(f'Högsta kastet var {highest_roll} ')
    print (f'Lägsta kastet var {lowest_roll}')

streak = int(0)

def main2():
    print ('Välkommen till gissningspelet!\n')
    gissningar = 0
    hemligtNummer = random.randint(1, 100)
    while True:
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

    if streak >= 3:
        print('Du har en grym strategi för att klara spelet!')



#user_input = get_menu_option() onödig?

while True:
    user_input = get_menu_option()

    if user_input == '1':
        print()
        print('Skapat av:')
        print('André, Ali och Christopher')

    if user_input == '2':
        main()

    if user_input == '3':
        main2()

    elif (user_input == '4'):
        print()
        print('See you soon!')
        exit()



