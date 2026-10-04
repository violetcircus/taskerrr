import json

class deck:
    cards = []
    name = ""
    desc = ""
    algo = ""
    def new_deck(name, desc):
        print("im a deck!", name, desc)

class card:
    name = ""
    desc = ""
    weight = 0
    def new_card(name, desc):
        print("im a card!", name, desc)

class main:
    decks = []
    def load_decks():
        with open("decks.json") as f:
            d = json.load(f)
            decks = d

    def start():
        load_decks()
        while true:
            print("press v to view a deck, press d to make a new deck")
            choice = input()
            match choice:
                case "v":
                    view_deck()
                case "d":
                    create_deck()

    def create_deck():
        done = false
        print("new deck name")
        name = input()
        print("deck description")
        desc = input()
        deck1 = deck.new_deck(name, desc)

        print("loading deck with cards...")

        while true:
            print("card 1 name:")
            name = input()
            print("card 1 desc:")
            desc = input()
            new_card = cards.new_card(name, desc)
            deck1.cards.append(new_card)
            print("done?")
            done_check = input()
            if done_check == "y":
                break
        decks.append(deck1)

    def view_deck():
        print("current decks:", decks) 

    start()
