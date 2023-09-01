import csv
import random
from Stack import Stack 
from Queue import Queue
from BinarySearchTree import BinarySearchTree
#This program can be used as a draw character cards simulator from a video game called Genshin Impact. This program can simulate drawing cards from the pool with different possibility(rarity) of each character. Users can test their luck before draw their character cards in the real game.It would be beneficial for the user to test their luck(and to not put so much money in it if they have a bad luck day).
#Character class:
  #class character is used for allowing binary search tree to compare charater names
        # str :character's name
        # str :character's region
        # str : character's rarity, ['NA','4','5']
#Genshin class:
      # store all characters
        # all cards with rarity NA obtained from lottery
        # all cards with rarity 5 obtained from lottery
        # all cards with rarity 4 obtained from lottery
class Character:
    def __init__(self, name, region, rarity):
        self.name = name
        self.region = region
        self.rarity = rarity

    # < 
    def __lt__(self,other):
        if isinstance(other,str):
            return self.name < other
        else:
            return self.name < other.name

    # ==
    def __eq__(self,other):
        if isinstance(other,str):
            return self.name == other
        else:
            return self.name == other.name

    # >
    def __gt__(self,other):
        if isinstance(other,str):
            return self.name > other
        else:
            return self.name > other.name


    def __repr__(self):
        return f"{self.name} is from {self.region} with rarity {self.rarity}"

class Genshin:
    all_characters = list()
  
    def __init__(self):
        self.characters_NA = Queue()
        self.characters_4 = Stack()
        self.characters_5 = BinarySearchTree()

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        # read csv file to instantiate characters and add them to all_characters
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for item in reader:#4 5 NA
                n = 6-int(item['rarity']) if item['rarity'].isdigit() else 3        
                for _ in range(n):
                    ch = Character(item['character_name'], item['region'], item['rarity'])
                    Genshin.all_characters.append(ch)

    def get_card(self,card):
        # add card to corresponding container by its rarity
        if card.rarity == "5":
            print(f"get a 5 star character {card.name}")
            self.characters_5.insert(card)
        elif card.rarity == "4":
            print(f"get a 4 star character {card.name}")
            self.characters_4.push(card)
        else:
            print(f"get a 3 star character {card.name}")
            self.characters_NA.enqueue(card)

    def draw_card(self):
        # draw a card randomly from all_characters
        card = random.choice(Genshin.all_characters)
        self.get_card(card)
    
    def draw_ten_card(self):
        # draw ten cards randomly from all_characters
        cards = [random.choice(Genshin.all_characters) for _ in range(10)]
        for card in cards:
            self.get_card(card)
 
    def description(self):
        # print the number of characters in each container
        print(f"5 star characters: {self.characters_5.size()}")
        print(f"4 star characters: {self.characters_4.size()}")
        print(f"Other characters: {self.characters_NA.size()}")
  
    def draw(self):
        # the menu for user to draw a card or ten cards
        print("1 Draw a card")
        print("2 Draw ten cards")
        print("0 Back")
        usr_input = input("Input your choice:\n")
        while usr_input !="0" :
            if usr_input == "1":
                self.draw_card()
            elif usr_input == "2":
                self.draw_ten_card()
            print("\n1 Draw a card")
            print("2 Draw ten cards")
            print("0 Back")
            usr_input = input("Input your choice:\n")

    def handle_5(self):
        # the menu for user to search, delete, or list characters in the BTS characters_5
        print("1 List your characters")
        print("2 Delete [name]")
        print("3 Search [name]")
        print("0 Back")
        usr_input = input("Input your choice:\n")
        while usr_input !="0" :
            if usr_input == "1":
                print(self.characters_5)
            elif usr_input == "2":
                del_name = input("input the name to delete:\n")
                if self.characters_5.remove(del_name):
                    print(f"The character {del_name} was deleted!")
                else:
                    print(f"The character {del_name} was not found!")
            elif usr_input == "3":
                srch_name = input("input the name to search:\n")
                node = self.characters_5.search(srch_name)
                if node is not None:
                    print(f"The character {srch_name} is {node.__repr__()}!")
                else:
                    print(f"The character {srch_name} was not found!")
            print("\n1 List your characters")
            print("2 Delete [name]")
            print("3 Search [name]")
            print("0 Back")
            usr_input = input("input your choice:\n")

    def handle_4(self):
        # the menu for user to list or delete characters in the stack characters_4
        print("1 List your characters")
        print("2 Delete the last one")
        print("0 back")
        usr_input = input("input your choice:\n")
        while usr_input !="0" :
            if usr_input == "1":
                print(self.characters_4)
            elif usr_input == "2":
                tmp = self.characters_4.pop()
                if tmp is None:
                    print("The stack is empty!")
                else:
                    print(f"The character {tmp.data.name} was deleted!")
            print("\n1 List your characters")
            print("2 Delete the last one")
            print("0 Back")
            usr_input = input("Input your choice:\n")

    def handle_other(self):
        # the menu for user to list or delete characters in the queue characters_NA
        print("1 List your characters")
        print("2 Delete the first one")
        print("0 Back")
        usr_input = input("Input your choice:\n")
        while usr_input !="0" :
            if usr_input == "1":
                self.characters_NA.print_queue()
            elif usr_input == "2":
                tmp = self.characters_NA.dequeue()
                if tmp is None:
                    print("The queue is empty!")
                else:
                    print(f"the character {tmp.data.name} was deleted!")
            print("\n1 List your characters")
            print("2 Delete the first one")
            print("0 Back")
            usr_input = input("Input your choice:\n")


if __name__ == '__main__':

    Genshin.instantiate_from_csv("genshin/genshin.csv")
    genshin = Genshin()
    print("1 Draw cards")
    print("2 Handle 5 star characters")
    print("3 Handle 4 star characters")
    print("4 Handle other characters")
    print("0 Exit")
    usr_input = input("Input your choice:\n")

    while usr_input != "0":
        if usr_input == "1":
            genshin.draw()
        elif usr_input == "2":
            genshin.handle_5()
        elif usr_input == "3":
            genshin.handle_4()
        elif usr_input == "4":
            genshin.handle_other()
        print("\n1 Draw cards")
        print("2 Handle 5 star characters")
        print("3 Handle 4 star characters")
        print("4 Handle other characters")
        print("0 Exit")
        usr_input = input("Input your choice:\n")