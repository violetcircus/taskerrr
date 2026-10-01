import json

class deck:
    cards = []
    name = ""
    desc = ""
    algo = ""
    def newDeck(name, desc):
        print("im a deck!", name, desc)
        pass

class card:
    name = ""
    desc = ""
    weight = 0
    def newCard(name, desc):
        print("im a card!", name, desc)
        pass

class main:
    decks = {}

    with open("decks.json") as f:
        d = json.load(f)
        decks = d

    print("current decks:", d) 

    print("new deck name")
    name = input()
    print("deck description")
    desc = input()
    deck1 = deck.newDeck(name, desc)

    print("load deck with cards.")
    print("card 1 name:")
    name = input()
    print("card 1 desc:")
    desc = input()
    new_card = cards.newCard(name, desc)
    deck1.cards.append(new_card)

