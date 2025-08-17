# Day 41 to Day 60 subroutines
from threading import main_thread


def day41(): # how to print dict properly
    print("🗝️ Day 41: I've Lost My Keys")
    # you need a for loop with two variable in a f string

    print("Website rating")

    webiste_rating = {}
    webiste_rating["name"] = input("Enter The Name of the website: ")
    webiste_rating["Url"] = input("Enter The URL: ")
    webiste_rating["description"] = input("Enter a brief description: ")
    webiste_rating["rate"] = input("Enter a rating : ")

    for name , value in webiste_rating.items():
        print(f"{name}:{value}")
        # any variables can work

def day42():
    print("🐾 Day 42: MokeBeast") # (pokemon), Challenge using dictionaries

    pokemon1= {"name": "" , "type": "" , "special_move": "" , "starting_hp": "" ,"energy": ""}

    pokemon1["name"] = input("Enter your Pokemons name: ")
    pokemon1["type"] = input("Enter your Pokemons type: ")
    pokemon1["special_move"] = input("Enter your Pokemons special move: ")
    pokemon1["starting_hp"] = input("Enter your Pokemons HP: ")
    pokemon1["energy"] = input("Enter your Pokemons Energy: ")
    print()
    
    for name , value in pokemon1.items():
        print(f"Your pokemons {name} is {value}")






def day43():
    print("📦 Day 43: Taking Lists to a New Dimension") # 2d lists
    # when accessing lists you do the row first then column as opposed to in maths where its x(colum) than y(row)
    # my_list[row][column] = data
    print("Bingo Generator")
    import random


    bingo_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # added 0 otherwise you will get a index out of range message

    for i in range(3):
        for j in range (3):
            bingo_list[i][j] = random.randint(1,90) # adds random numbers to a 2d list

    bingo_list [1][1] = "Bingo" # bingo games have the word bingo in the middle

    for i in range(3):
        print(bingo_list[0][i],end=" ")

    print()

    for i in range(3):
        print(bingo_list[1][i], end=" ")

    print()

    for i in range(3):
        print(bingo_list[2][i], end=" ")

    print()
    print()





def day44():
    import  random
    print("🧮 Day 44: Dynamic 2D Lists")
    print("full game of bingo")

    def init_board():
        bingo_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # added 0 otherwise you will get a index out of range message

        for i in range(3):
            for j in range(3):
                bingo_list[i][j] = random.randint(1, 90)  # adds random numbers to a 2d list

        bingo_list[1][1] = "Bingo"  # bingo games have the word bingo in the middle

        for i in range(3):
            print(bingo_list[0][i], end=" ")

        print()

        for i in range(3):
            print(bingo_list[1][i], end=" ")

        print()

        for i in range(3):
            print(bingo_list[2][i], end=" ")

        return bingo_list


    def print_board():
        for i in range(3):
            print(bingo_list[0][i], end=" ")
        print()
        for i in range(3):
            print(bingo_list[1][i], end=" ")
        print()
        for i in range(3):
            print(bingo_list[2][i], end=" ")

    no_x = 0
    while True:
        print()
        bingo_list = init_board()
        print()
        print()

        fine = input(" Does the board have duplicates? ")

        if fine.lower() == "no":
            break
        else:
            continue

    while True:
        num = int(input("What number did you get: "))

        if any(num in row for row in bingo_list):
            print("That number is in the list, Well done")

            for i in range(3):
                for j in range(3):
                    if num == bingo_list[i][j]:
                        row = i
                        column = j
                        bingo_list[i][j] = "X"

                        print_board()
                        print()
                        print()
                        no_x = no_x +1
                        break



        else:
            print("That number doesnt exist in the bingo list ,Sorry")
            print()

        if no_x == 8:
            print()
            print("BINGO")
            break

def day45(): # to do list with priorities
    import time
    print("✅ Day 45: Get it 'to done'!")

    to_do = [["Task Name", "Priority", "Due"]] # creates a 2d list with headings

    def add():
        print()
        print("Adding Tasks")

        title =input("Enter the tasks name: ")
        priority  = input("Enter the priority: ")
        due = input("Enter Due Date in dd/mm/yyyy: ")

        row = [title,priority,due] # 2d list is created here
        to_do.append(row)


    def view():
        rows = len(to_do)
        print("What do you want to sort by? (Priority or Date of Entry)")
        sort = input("Enter p /de")


        if sort.lower() == "p":

            high_priority_list = []  # x_priority_list stores the location of each corresponding priority
            medium_priority_list = []
            low_priority_list = []
            other_priority_list = []


            for i in range (rows):

                if to_do[i][1].lower() == "high":  #x_priority gets the location of each corresponding priority
                    high_priority_list.append(i)

            for i in range (rows):
                if to_do[i][1].lower() == "medium":
                    medium_priority_list.append(i)

            for i in range (rows):
                if to_do[i][1].lower() == "low":
                    low_priority_list.append(i)

            for i in range (rows):
                if to_do[i][1].lower() not in ["low", "medium", "high"]:
                    low_priority_list.append(i)

            high_priority_len = len(high_priority_list)
            medium_priority_len = len(medium_priority_list)
            low_priority_len = len(low_priority_list)
            other_priority_len = len(other_priority_list)

            for i in range(high_priority_len): # prints high priority first
                for item in to_do[high_priority_list[i]]:
                    print(item, end=" | ")
                print()

            for i in range(medium_priority_len):
                for item in to_do[medium_priority_list[i]]:
                    print(item, end=" | ")
                print()

            for i in range(low_priority_len):
                for item in to_do[low_priority_list[i]]:
                    print(item, end=" | ")
                print()

            for i in range(other_priority_len):
                for item in to_do[other_priority_list[i]]:
                    print(item, end=" | ")
                print()


        else:
            for row in to_do:
                for item in row :
                    print(item,end=" | ")
                print()



    def delete():
        to_delete = input("What task would you like to delete: ")


        for i in range(len(to_do)):
            if to_do[i][0].lower() == to_delete.lower():
                del to_do[i] #delted here


    def menu():
        print()
        print("1. For adding an item")
        print("2. For viewing your list")
        print("3. For deleting an item ")


        choice = int(input("What is your choice: "))
        time.sleep(0.5)

        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            delete()

        else:
            print("Not a valid choice")
            print()
            menu()

    while True:
        exit = input("Do you want to exit: ")
        if exit.lower() == "yes":
            break

        menu()


def day46(): #creating a 2D Dictionary
    print("📚 Day 46: Dictionaries are Back...")
    pokemon={}

    while True:

        name = input("Enter your Pokemons name: ")
        type = input("Enter your Pokemons type: ")
        special_move  = input("Enter your Pokemons special move: ")
        starting_hp= input("Enter your Pokemons HP: ")
        energy = input("Enter your Pokemons Energy: ")

        pokemon[name] = {"type":type , "special_move":special_move , "starting_hp":starting_hp , "energy":energy }
        # uses the name as the identifier for the dictionary

        print()
        if input("Add another Pokemon (y/n): ").lower() == "n" :
            break # more efficient don't need to store any variables

    print()
    for key, value in pokemon.items():
        print(f"{key:^12} | {value["type"]:^10} | {value["special_move"]:^12} | {value["starting_hp"]:^4} | {value["energy"]}:^5|")
        # key is the name of the pokemon
        # value["xxx"] specify which 2nd value to retrieve
        # ^n center alllings a number 

def day47(): # Challenge create TOP Trumps  using 2D-dicts
    import  time
    print("🎴 Day 47: Top Trumps")

    top_trump_char = {
        "Starter_Boi": {"power": 60, "hp": 60},
        "Speedy_Boi": {"power": 30, "hp": 30},
        "Heavy_Boi": {"power": 80, "hp": 55},
        "Balanced_Boi": {"power": 50, "hp": 50}}

    print("These are the Character that you can choose")
    print("Chose Wisely")
    time.sleep(0.5)
    print()
    for key , value in top_trump_char.items():
        print(key)

    player_choice = input("Who do you chose: ")

    if player_choice.lower() == "starter" or "starter boi" or "starter_boi":
        print(f"{top_trump_char["Starter_Boi"]} ")


def day48():
    print("🏆 Day 48: Saving to Files")


def day49():
    print("📖 Day 49: Reading a File")


def day50():
    print("💡 Day 50: Idea Storage")


def day51():
    print("💾 Day 51: You Save Your Data in...")


def day52():
    print("🛡️ Day 52: Brace for Impact")


def day53():
    print("🎮 Day 53: Video Game Inventory")


def day54():
    print("📊 Day 54: Comma', 'Separated'...What?!")


def day55():
    print("🔙 Day 55: Back the 'f' up?!")


def day56():
    print("🎧 Day 56: Music Streaming Service")


def day57():
    print("🔁 Day 57: Recursion")


def day58():
    print("🐞 Day 58: Debugger")


def day59():
    print("🔤 Day 59: Palindrome")


def day60():
    print("⏳ Day 60: The Magic of Time")


# Main loop
while True:
    day = input("Enter a day number (41–60), or 'exit' to quit: ")
    if day.lower() == "exit":
        break
    elif day.isdigit() and 41 <= int(day) <= 60:
        eval(f"day{day}()")
    else:
        print("Invalid input. Please enter a number between 41 and 60.")
