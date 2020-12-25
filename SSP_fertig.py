import random as rnd

runde = 1
player1 = 0
player2 = 0
Wahl1 = 0
Wahl2 = 0

print("Willkommen zu Schere Stein Papier\n")

print("Für Schere: 1")
print("Für Stein: 2")
print("Für Papier: 3")


while player1 != 3 and player2 != 3:

    #Spieler 1
    print("\n----------------\n")

    print("Runde", runde)
    Wahl1 = int(input("Deine Wahl: "))

    #Spieler 2

    Wahl2 = rnd.randint(1,3)
    #Wer hat die Runde gewonnen?

    if Wahl1 == Wahl2:
        print("Unentschieden")
        runde += 1
        player1 += 1
        player2 += 1
    else:
        if Wahl1 == 1:                                  #Spieler wählt Schere
            if Wahl2 == 3:
                player1 += 1
                print("Spieler 1 gewinnt diese Runde (Schere schlägt Papier)")
                runde += 1
            else:
                player2 += 1
                print("Spieler 2 gewinnt diese Runde (Stein schlägt Schere)")
                runde += 1

        elif Wahl1 == 2:                                #Spieler wählt Stein
            if Wahl2 == 1:
                player1 += 1
                print("Spieler 1 gewinnt diese Runde (Stein schlägt Schere)")
                runde += 1
            else:
                player2 += 1
                print("Spieler 2 gewinnt diese Runde (Papier schlägt Stein)")
                runde += 1
        elif Wahl1 == 3:                                  #Spieler wählt Papier
            if Wahl2 == 2:
                player1 += 1
                print("Spieler 1 gewinnt diese Runde (Papier schlägt Stein)")
                runde += 1
            else:
                player2 += 1
                print("Spieler 2 gewinnt diese Runde (Schere schlägt Papier)")
                runde += 1
        else:
            print("Fehler-1")
else:
    print("\n------------------------")
    if player1 == 3:
        print("Spieler 1 hat gewonnen !")
    elif player2 == 3:
        print("Spieler 2 hat gewonnen !")
    else:
        print("Fehler-2")
print("------------------------\n")
input("Enter zum beenden")