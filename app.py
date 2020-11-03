import sys
import keyboard


class Lager:
    def __init__(self, namn, pris, antal):
        self.namn = namn
        self.pris = pris
        self.antal = antal


with open('test.txt', 'r') as myFile:


count = 0
lagerList = []
lagerList.append(Lager("Playstation 5 (Physical Edition)", "5990", "5"))
lagerList.append(Lager("Playstation 5 (Digital Edition)", "4990", "3"))
lagerList.append(Lager("BloodBorne Kart", "420", "Slutsåld"))


dictb = {}

for lager in lagerList:
    dictb[lager] = "{}".format(lager.namn)


def addEntry():
    entry = Lager(input("Namn på produkten: "), input(
        "Pris på produkten: "), input("Lagerstatus: "))
    lagerList.append(entry)


def showLogic():
    for lager in lagerList:
        count = int()
        count = str(count)
        print(count + ': ' + '{}\n{} SEK\nLagerstatus: {}\n'.format(
            lager.namn, lager.pris, lager.antal))


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
            break
    except:
        break

print("Vill du lägga till eller ta bort en artikel?")
for i in dictb:
    count = int(count + 1)
    print(str(count) + ": " + dictb[i])

with open('test.txt', 'w') as myFile:
    count = 0
    for i in dictb:
        count = int(count + 1)
        myFile.write(str(count) + ": " + dictb[i]+"\n")

# while True:
#   try:
#      if keyboard.is_pressed('y'):
#         for lager in lagerList:
#            count = int(count + 1)
#           str(count)
#          print(count + ': ' + '{}\n{} SEK\nLagerstatus: {}\n'.format(
#             lager.namn, lager.pris, lager.antal))
# else:
#   break
