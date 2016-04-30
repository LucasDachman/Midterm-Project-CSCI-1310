"""
Lucas Dachman
Final Project
9/29/15

This is a Dungeon Game!
"""

import sys


def main(argv):
    Start.play(None)


class Start:
    """Start"""

    @staticmethod
    def play(last):
        last_key = ""
        while last_key not in ["p", "k", "r", "q"]:
            last_key = input("You are walking home with a special package. A man in a hoodie runs up to you and tries to take your package.\nPunch(p), Kick(k), Run Away(r)")
        if last_key == "p":
            print("The hooded man blocks your punch and knocks you to the ground. He takes your package and runs off. You get up and follow him to a huge house. You HAVE to get your package back.")
        elif last_key == "k":
            print("You try to roundhouse kick the man but he grabs your leg and throws you to the ground. He takes your package and runs off. You get up and follow him to a huge house. You HAVE to get your package back.")
        elif last_key == "r":
            print("You try to run but the man trips you and you fall to the ground. He takes your package and runs off. You get up and follow him to a huge house. You HAVE to get your package back.")
        elif last_key == "q":
            next_room("q", Start.play)

        print("If you enter the house, you may not come back out...")
        last_key = ""
        while last_key not in ["q", "y", "n"]:
            last_key = input("Would you like to enter? (y/n)")
            if last_key == "y":
                Hallway.play(None)
        print("Goodbye")


class Hallway:
    """Hallway"""

    @staticmethod
    def play(last):
        last_key = input("You are in the Hallway. There are doors to the West(w), North(n) and East(e).")
        next_room(last_key, Hallway.play, Kitchen.play, LivingRoom.play, Office.play, Hallway.play)


class Kitchen:
    """Kitchen"""

    knife_taken = False

    @staticmethod
    def play(last):
        print("You are in the kitchen. The chef is making food.")
        last_key = ""
        while last_key not in ["l", "q"]:
            if not Kitchen.knife_taken:
                last_key = input("Ask him who lives here?(a), Ask what he's making?(b), Knock him out and take his knife?(k), Leave?(l)")
                if last_key == "a":
                    print("\"We don't talk about that. You shouldn't be asking questions. They only lead to trouble.\"")
                elif last_key == "b":
                    print("\"It's a special recipe. I doubt you'll be able to stay for dinner though.\"")
                elif last_key == "k":
                    Kitchen.knife_taken = True
                    print("You knock him out with your shoe and take his knife.")
            else:
                while last_key != "l":
                    last_key = input("The chef is knocked out on the floor. Leave?(l)")
        if last_key == "q":
            next_room("q", Kitchen.play)
        elif last_key == "l":
           last(Kitchen.play)


class LivingRoom:
    """Living Room"""

    @staticmethod
    def play(last):
        last_key = input("You are in the Living Room, There are doors to the East(e) and South(s) and stairs to the North(n). ")
        next_room(last_key, LivingRoom.play, LivingRoom.play, Stairs.play, Bedroom.play, Hallway.play)


class Stairs:
    """Stairs"""

    broken = False

    @staticmethod
    def play(last):
        last_key = ""
        if last is TopHallway.play:
            print("You forgot about the trapped door! You fall into the basement.")
            Basement.play(None)
        elif Stairs.broken:
            while last_key not in ["d", "b", "q"]:
                last_key = input("The stairs to the second floor are broken. Go down to the basement(d) or back to living room?(b) ")
        else:
            while last_key not in ["u", "d", "b", "q"]:
                last_key = input("Go up, down, or back? (u/d/b)")
        if last_key == "u":
            print("As you walk up the stairs you hear noises. It sounds like some kind of machine. By the time you realize what is going on, it's too late. You fall through a trapped door into the basement.")
            Stairs.broken = True
            Basement.play(None)
        elif last_key == "d":
            Basement.play(None)
        elif last_key =="b":
            LivingRoom.play(Stairs.play)
        elif last_key == "q":
            next_room("q", TopHallway.play)


class Basement:
    """Basement"""

    @staticmethod
    def play(last):
        print("You are in the Basement.")
        last_key = ""
        while last_key not in ["s","q"]:
            last_key = input("Go up the stairs?(s) ")
        if last_key == "s":
            Stairs.play(None)
        elif last_key == "q":
            next_room("q", Basement.play)

class Bedroom:
    """Bedroom"""

    maid_dead = False

    @staticmethod
    def play(last):
        last_key = ""
        while last_key != "l" and not Bedroom.maid_dead:
            last_key = input(
                """You are in the Bedroom. You see a maid dusting some vases. She doesn't notice you.
                Ask if she knows who lives here(a)
                Ask where your package is(b)
                Knock her out and search her pockets(k)
                Leave(l)""")
            if last_key == "a":
                print("\"We're not supposed to talk about that, sorry. You shouldn't be here.\"")
            elif last_key == "b":
                print("\"I have no idea what you are talking about. If I were you, I'd leave now.\"")
            elif last_key == "k":
                print("You knock her out with your shoe. In her pockets, you find a gold key. You decide the key might be important so you take it. ")
                Bedroom.maid_dead = True
                Office.locked = False
            elif last_key == "q":
                next_room("q", Bedroom.play)
        while last_key not in ["l", "i", "q"]:
            if not Stairs.broken:
                last_key = input("You are in the Bedroom. The maid is on the floor knocked out. Leave(l)")
            else:
                last_key = input("You are in the Bedroom. The maid is on the floor knocked out. There is a bookshelf on the North side of the room. Inspect bookshelf(i) or leave(l)?")
        if last_key == "l":
            last(last)
        elif last_key == "i":
            Bookshelf.play(Bedroom.play)
        elif last_key == "q":
            next_room("q", Bedroom.play)


class Bookshelf:
    """Bookshelf"""

    @staticmethod
    def play(last):
        last_key = ""
        while last_key not in ["1", "2", "3", "4", "5", "q"]:
            last_key = input("""You look at the books.
            1. The Lord Of The Rings, JRR Tolkien
            2. Don Quixote, Miguel de Cervantes
            3. Harry Potter and the Sorcerer's Stone, JK Rowling
            4. To Kill a Mockingbird, Harper Lee
            5. Ender's Game, Orson Scott Card
            Inspect book? (1-5)
            """)
        if last_key == "5":
            last_key = input("You pull on the book but it doesn't come all the way off the shelf. The bookshelf opens to reveal a staircase leading upstairs. Go upstairs(s) or go back(b)? ")
            if last_key == "s":
                TopHallway.play(None)
            elif last_key == "b":
                last(None)
        elif last_key in ["1","2","3","4"]:
            print("It's just a book. You put it back.")
            Bookshelf.play(last)
        elif last_key == "q":
            next_room("q", Bookshelf.play)


class TopHallway:
    """Upstairs Hallway"""

    @staticmethod
    def play(last):
        last_key = ""
        last_key = input("You are in the Upstairs Hallway. There is a door to the West(w) and South(s). Also there are stairs to the North(n) and East(e). ")
        next_room(last_key, TopHallway.play, Bathroom.play, Stairs.play, Bedroom.play, Lab.play)


class Bathroom:
    """Bathroom"""

    @staticmethod
    def play(last):
        print("\"Occupied!!\" Must be a bathroom...")
        last(None)


class Lab:
    """Lab"""

    @staticmethod
    def play(last):
        print("You look around the room you just entered. It seems to be some sort of laboratory. Unlike the rest of the house, this room is clean and modern. The hooded man is there. He puts down your package and reaches for the gun on his hip.")
        last_key = ""
        if Office.gun_taken and Kitchen.knife_taken:
            while last_key not in ["s", "r", "c", "q"]:
                last_key = input("Shoot the man with the gun from the office?(s), Charge the man and attack him with the knife?(c)  or run?(r)")
        elif Office.gun_taken:
            while last_key not in ["s", "r"]:
                last_key = input("Shoot the man with the gun from the office?(s) or run?(r)")
        elif Kitchen.knife_taken:
            while last_key not in ["c", "r"]:
                last_key = input("Charge the man and attack him with the knife?(c) or run?(r)")
        else:
            while last_key not in ["t", "r"]:
                last_key = input("Run(r) or tackle the man(t)?!")
        if last_key in ["t", "r", "c"]:
            print("You are too slow. The man shoots you and keeps the package. You have failed...")
        elif last_key == "q":
            next_room("q", Lab.play)
        else:
            print("You shoot the man before he can reach his gun. You take the package and leave. Congratulations, you won.")



class Office:
    """Office"""

    locked = True
    gun_taken = False

    @staticmethod
    def play(last):
        if Office.locked:
            print("The door is locked. There must be a key somewhere in the house...")
            input()
            last(Office.play)
        else:
            print("You use the gold key to unlock the door. The room is an office.")
            last_key = ""
            while last_key not in ["i", "l", "q"]:
                last_key = input("There is a desk. Inspect the drawers(i) or leave(l)?")
            if last_key == "i":
                if not Office.gun_taken:
                    while last_key not in ["y", "n"]:
                        last_key = input("There is a gun in the drawer. Take the gun? (y/n) ")
                    if last_key == "y":
                        Office.gun_taken = True
                else:
                    print("There is nothing interesting in the drawer.")
                while last_key !="l":
                    last_key = input("leave?(l) ")
            elif last_key == "q":
                next_room("q", Office.play)
            last(None)


def next_room(key, repeat=None, west=None, north=None, east=None, south=None):
    if key == "w":
        west(repeat)
    elif key == "n":
        north(repeat)
    elif key == "e":
        east(repeat)
    elif key == "s":
        south(repeat)
    elif key == "q":
        if input("quit?(y/n)") == "y":
            print("Goodbye!")
            sys.exit()
        else:
            repeat(repeat)
    else:
        repeat(repeat)

main(sys.argv)