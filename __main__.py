import json

decks = {}
DECKS_FILE = "decks.json"

class Deck(dict):
    def __init__(self, name, desc, algo = "", cards: List[Card] = []):
        dict.__init__(self, name=name, desc=desc, algo=algo, cards = cards)
        self.name = name
        self.desc = desc
        self.algo = algo
        self.cards = cards

class Card(dict):
    def __init__(self, name, desc, weight = 0):
        dict.__init__(self, name=name, desc=desc, weight=weight)
        self.name = name
        self.desc = desc
        self.weight = 0

def load_decks():
    with open(DECKS_FILE) as f:
        deck_file = json.load(f)
        for k in deck_file.keys():
            d = deck_file[k]
            card_objects = []
            for c in d["cards"]:
                card_objects.append(Card(**c))
            deck = Deck(
                name = d["name"],
                desc = d["desc"],
                algo = d["algo"],
                cards = card_objects
            )
            decks[d["name"]] = deck

def view_cards(deck):
    for c in deck.cards:
        print("-------------")
        print(c.name)
        print(c.desc)
        print("-------------")

def view_deck():
    print("current decks:", decks.keys()) 
    print("which deck?")
    choice = input()
    print("-------------")
    deck = decks[choice]
    print(deck.name)
    print(deck.desc)
    print("cards:")
    view_cards(deck)

def start():
    while True:
        print("press v to view a deck, press d to make a new deck")
        choice = input()
        match choice:
            case "v":
                view_deck()
            case "d":
                create_deck()

def save_decks():
    with open(DECKS_FILE, "w") as f:
        json.dump(decks, f, ensure_ascii=False, indent=2)

def create_deck():
    print("new deck name")
    name = input()
    print("deck description")
    desc = input()
    new_deck = Deck(name, desc)

    print("loading deck with cards...")

    while True:
        print("card 1 name:")
        card_name = input()
        print("card 1 desc:")
        card_desc = input()
        new_card = Card(card_name, card_desc)
        new_deck.cards.append(new_card)
        print("done?")
        done_check = input()
        if done_check == "y":
            break
    decks[name] = new_deck
    save_decks()

load_decks()
start()
