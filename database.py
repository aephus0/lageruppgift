import pymongo
import json
pw = str(input("Please enter the Staging-User password: "))


client = pymongo.MongoClient(
    "mongodb+srv://staging-user:{}@varor.igatz.mongodb.net/varor?retryWrites=true&w=majority".format(pw))
db = client["Varor-Database"]
col = db["Varor"]

pw = None
lagerlist = []
test = {}


class Lager:
    def __init__(self, name, count, price, adress="-"):
        self.name = name
        self.count = count
        self.price = price
        self.adress = adress


def showLogic():
    for x in col.find():
        print(x)


def addEntry():
    lagerlist.append(
        Lager(input("Namn: "), input("Antal: "), input("Pris: ")))

    for lager in lagerlist:
        test[lager] = "{}#{}#{}#{}".format(
            lager.name, lager.count, lager.price, lager.adress)

    print(test)
    x = json.dumps(test, skipkeys=True, separators='#' ',')
    print(x)
    x = json.load(x)
    print(x)

    # col.insert_one(x)
    # print(x.inserted_ids)


#x = col.insert_one(test)
showLogic()
addEntry()
showLogic()
