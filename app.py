
class Lager:
    def __init__(self, namn, pris, antal):
        self.namn = namn
        self.pris = pris
        self.antal = antal


lagerList = []
lagerList.append(Lager("Playstation 5 (Physical Edition)", "5990 SEK", "5"))
lagerList.append(Lager("Playstation 5 (Digital Edition)", "4990 SEK", "3"))
lagerList.append(Lager("BloodBorne Kart", "420 SEK", "Slutsåld"))
for lager in lagerList:
    print('{}\n{}\nLagerstatus: {}\n'.format(
        lager.namn, lager.pris, lager.antal))
