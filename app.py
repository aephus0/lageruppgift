import sys
from sys import path
from time import time
import keyboard
import os
import json
import time
import os.path
from keyboard import wait

lagerList = []
test = {}
dictb = {}
count = 0


def clear():
    os.system('cls')


class Lager:
    def __init__(self, namn, pris, antal):
        self.namn = namn
        self.pris = pris
        self.antal = antal


def addEntry():
    lagerList.append(Lager(str(input("Namn på produkten: ")), str(input(
        "Pris på produkten: ")), str(input("Lagerstatus: "))))

    for lager in lagerList:
        dictb[lager] = "{}#{}#{}".format(
            lager.namn, lager.pris, lager.antal)

    with open('test.txt', 'w') as temp:
        for i in dictb:
            temp.write(str(dictb[i]))


def removeEntry():
    print("Please enter the name of the item you wish to remove. NOTE: Write the EXACT name of the item!")
    tempInput = str(input())
    dictb.pop(tempInput, None)
    for key in dictb:
        lagerList[key] = ("{}{}{}".format(key.namn, key.pris, key.antal))

    with open('test.txt', 'w') as temp:
        for i in dictb:
            temp.write(str(dictb[i]))


def showLogic():
    for lager in lagerList:
        count = int(count + 1)

        print(str(count) + ': ' + '{}\n{} SEK\nLagerstatus: {}\n'.format(
            lager.namn, lager.pris, lager.antal))


if os.path.isfile('test.txt'):
    print("'test.txt' found!")
else:
    print("'test.txt' not found, creating file now...")
    with open('test.txt', 'w') as create:
        pass

try:
    with open('test.txt', 'r') as myFile:
        if os.stat('test.txt').st_size == 0:
            print("Cannot read contents of file. Maybe the file is empty?")
        elif not os.stat('test.txt').st_size == 0:
            with open('test.txt', 'r') as tempFile:

                for line in tempFile:
                    (key, val1, val2) = line.split("#")
                    test[key] = val1, val2
                    lagerList.append((Lager(key, val1, val2)))

except FileNotFoundError:
    print("File cound not be opened. File is missing or could be corrupted!")
    print("Press 'ENTER' to exit the program.")
    keyboard.wait('enter')
    sys.exit()


print("Visa lager?")
print("Y/y för 'JA' och N/n för 'NEJ'\n")

while True:
    try:
        if keyboard.is_pressed("y"):

            if os.stat('test.txt').st_size == 0:
                print("No items to show!")
            else:
                showLogic()
            break
        elif keyboard.is_pressed("esc"):
            sys.exit()
    except:
        sys.exit()

print("Vill du lägga till eller ta bort en artikel?")

removeEntry()

while True:
    try:
        if keyboard.is_pressed("y"):
            for lager in lagerList:
                count = int(count + 1)
                str(count)
                print(count + ': ' + '{}\n{} SEK\nLagerstatus: {}\n'.format(
                    lager.namn, lager.pris, lager.antal))
                break
        elif keyboard.is_pressed("esc"):
            sys.exit()
    except:
        sys.exit()
