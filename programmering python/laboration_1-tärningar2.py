import random


def roll_dice():      #Simulering av 2st tärningskast
    return random.randint(2, 12)


def main():
    print("Välkommen till tärningsspelet!")

    rundor = int(input("Skriv in antalet rundor du vill spela: "))

    spelarPoäng = 0     #Vad varje spelare börjar med
    aiPoäng = 0
    spelarKasten = []    #Listan där varje spelares kast kommer sparas
    aiKasten = []

    for antalRundor in range(1, rundor + 1):    #börjar på runda 1, därav +1 i tak)
        input(f"\n>> Runda {antalRundor} <<\nTryck Enter för att slå tärningen...")

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

                                            #Avgörandet om vem som vinner
    print("\n-- Matchen är över --")
    print(f"Final Score - You: {spelarPoäng}, AI: {aiPoäng}")

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







main()

