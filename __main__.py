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

# file handling stuff 
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

def save_decks():
    with open(DECKS_FILE, "w") as f:
        json.dump(decks, f, ensure_ascii=False, indent=2)

def add_cards(deck):
    while True:
        print("card name:")
        card_name = input()
        print("card desc:")
        card_desc = input()
        new_card = Card(card_name, card_desc)
        deck.cards.append(new_card)
        print("done?")
        done_check = input()
        if done_check == "y":
            break

def view_cards(deck):
    for c in deck.cards:
        print("-------------")
        print(c.name)
        print(c.desc)
        print("-------------")

def view_deck():
    print("which deck?")
    choice = input()
    print("-------------")
    deck = decks[choice]
    print(deck.name)
    print(deck.desc)
    print("cards:")
    view_cards(deck)

def create_deck():
    print("new deck name")
    name = input()
    print("deck description")
    desc = input()
    new_deck = Deck(name, desc)

    print("loading deck with cards...")

    add_cards(new_deck)
    decks[name] = new_deck
    save_decks()

def edit_deck():
    print("which deck?")
    choice = input()

    deck = decks[choice]

    print("edit [n]ame, [d]esc, or [c]ards?")
    choice = input()
    match choice:
        case "n":
            print("current name:", deck.name)
            print("enter new name:")
            deck.name = input()
        case "d":
            print("current desc:", deck.desc)
            print("enter new desc:")
            deck.desc = input()
        case "c":
            print("[a]dd cards or [c]hange a card?")
            choice = input()
            match choice:
                case "a":
                    add_cards(deck)
                    print("done adding cards to", deck.name)
                case "c":
                    while True:
                        print("pick a card, any card")
                        view_cards(deck)
                        choice = int(input())

                        card = deck.cards[choice]

                        print("edit [n]ame or [d]esc?")
                        match input():
                            case "n":
                                print("current name:", card.name)
                                print("enter new name:")
                                card.name = input()
                            case "d":
                                print("current desc:", card.desc)
                                print("enter new desc:")
                                card.desc = input()
                        print("done?")
                        if input() == "y":
                            break
    print("lalala")
    save_decks()

def start():
    while True:
        print("current decks:", decks.keys()) 
        print("[v]iew, [e]dit or [c]reate a deck?")
        choice = input()
        match choice:
            case "v":
                view_deck()
            case "d":
                create_deck()
            case "e":
                edit_deck()

load_decks()
start()
