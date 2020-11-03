import sys
import keyboard

count = 0


class Lager:
    def __init__(self, namn, pris, antal):
        self.namn = namn
        self.pris = pris
        self.antal = antal


lagerList = []
lagerList.append(Lager("Playstation 5 (Physical Edition)", "5990", "5"))
lagerList.append(Lager("Playstation 5 (Digital Edition)", "4990", "3"))
lagerList.append(Lager("BloodBorne Kart", "420", "Slutsåld"))


def addEntry:
    entry = Lager(input("Namn på produkten: "), input(
        "Pris på produkten: "), input("Lagerstatus: "))
    lagerList.append(entry)


print("Visa lager?")
print("Y/y för 'JA' och N/n för 'NEJ\n'")

while True:
    try:
        if keyboard.is_pressed("y"):
            for lager in lagerList:

                print('{}\n{} SEK\nLagerstatus: {}\n'.format(
                    lager.namn, lager.pris, lager.antal))
            break
        elif keyboard.is_pressed("n"):
            sys.exit()
            break
    except:
        break

print("Vill du lägga till eller ta bort en artikel?")

while True
try:
    if keyboard.is_pressed('y')
    count = int(count + 1)
    for lager in lagerList:
        print('{}\n{} SEK\nLagerstatus: {}\n'.format(
            lager.namn, lager.pris, lager.antal))
