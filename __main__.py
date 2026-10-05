import json

decks = []

class Deck:
    def __init__(self, name, desc, algo, cards: List[Card]):
        # print("im a deck! name: ", name, desc)
        self.name = name
        self.desc = desc
        self.algo = algo
        self.cards = cards


class Card:
    def __init__(self, name, desc, weight):
        # print("im a card! name: ", name, desc)
        self.name = name
        self.desc = desc
        self.weight = 0

def load_decks():
    with open("decks.json") as f:
        deck_file = json.load(f)
        for d in deck_file:
            card_objects = []
            for c in d["cards"]:
                card_objects.append(Card(**c))
            deck = Deck(
                name = d["name"],
                desc = d["desc"],
                algo = d["algo"],
                cards = card_objects
            )
            decks.append(deck)

def view_deck():
    print("current decks:", decks) 
    print("which deck?")
    choice = int(input())
    print(decks[choice].name)
    print(decks[choice].desc)
    print(decks[choice].cards)

def start():
    while True:
        print("press v to view a deck, press d to make a new deck")
        choice = input()
        match choice:
            case "v":
                view_deck()
            case "d":
                create_deck()

def create_deck():
    print("new deck name")
    name = input()
    print("deck description")
    desc = input()
    deck1 = Deck(name, desc)

    print("loading deck with cards...")

    while True:
        print("card 1 name:")
        name = input()
        print("card 1 desc:")
        desc = input()
        new_card = Card(name, desc)
        deck1.cards.append(new_card)
        print("done?")
        done_check = input()
        if done_check == "y":
            break
    decks.append(deck1)

load_decks()
start()
