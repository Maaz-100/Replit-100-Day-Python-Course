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

def day45():
    print("✅ Day 45: Get it 'to done'!")


def day46():
    print("📚 Day 46: Dictionaries are Back...")


def day47():
    print("🎴 Day 47: Top Trumps")


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
