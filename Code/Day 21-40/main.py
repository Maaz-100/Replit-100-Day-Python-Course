def day_21():  # for loop + maths skills
    print()
    print("Entering Day 21")
    print("Multiplication tables")

    table = int(input("Enter the number you wanted to be tested on: "))
    end = int(input("Enter how many questions do you want : "))
    end = (table * end) + table
    correct = 0
    j = 0  # made j as another counter to show multplier

    for i in range(0, end, table):
        ans = int(input(
            f"what is {table} x {j}  = "))  # using f strings as normal strings wont support variable in input lines
        if ans == i:
            print("Correct")
            print("")
            correct += 1
        else:
            print("Wrong correct answer is ", i)
        j += 1

    print(f"you got  {correct}")  # starting to like F strings may use them more


def day_22():  # starting to use libraries
    import random
    print()
    print("Entering Day 22")
    print("Guessing game 2.0")

    to_guess = random.randint(1, 1000000)
    attempt = 0

    while True:
        guess = int(input("enter a number: "))

        if guess > to_guess:
            print("Lower")
            attempt += 1

        elif guess < to_guess:
            print("higher")
        elif to_guess == guess:
            print("well done you guessed it and it took ", attempt, " attempt(s)")


def day_23():  # subroutines
    print()
    print("Entering Day 23")

    def login():
        print("")
        print("Welcome")

    while True:
        name = input("Enter Your Name: ")
        password = int(input("Enter Your Password: "))
        if (name == "john") and (password == 1234):
            login()
            break
        else:
            print("Wrong name or password")
            print()


def day_24():  # passing parameters to subroutines
    print()
    print("Entering Day 24")
    print("Infinity dice")

    def roll_dice(sides):
        import random
        print("rolling dice")
        print(random.randint(1, sides))

    while True:
        print("")
        stop = input("stop? ")
        if stop == "yes":
            break
        sides = int(input("how many sides do you want on your dice:"))
        roll_dice(sides)


def day_25():  # return function

    print()
    print("Entering Day 25")
    print("health stats generator")

    def roll_6_and_8():
        import random
        dice = (random.randint(1, 6)) * (random.randint(1, 8))
        return dice

    while True:
        name = input("Enter your characters name or enter no to stop: ")

        if name.lower() == "no":
            break

        print(f"Characters {name} , HP: {roll_6_and_8()}")
        print()


def day_26():  # Using OS library

    # This is the code I am given to build on
    # import os
    # import time

    # import pygame

    # pygame.init()
    # pygame.mixer.init()
    # sound = pygame.mixer.Sound('audio.wav')
    # sound.play()

    # def pause():
    # pygame.mixer.pause()

    # pause()

    # def play():
    # Play the sound
    # pygame.mixer.unpause()
    # while True:
    # Start taking user input and doing something with it
    # input()

    # while True:
    # # clear the screen 

    # # Show the menu

    # #take user's input

    # # check whether you should call the play() subroutine depending on user's input
    # if True:
    #    play() 

    import os, pygame, time

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('audio.wav')
    sound.play()

    def pause():
        pygame.mixer.pause()
        while True:
            print(("Enter 1 to resume"))
            print(("Enter 2 to go to menu"))

            choice = int(input())
            if choice == 1:
                play()
            elif choice == 2:
                menu()
            else:
                print("Enter 1 or 2")

    def play():
        pygame.mixer.unpause()  # Play the sound

        while True:
            choice = int(input("Press 1 to stop: "))
            if choice == 1:
                pause()
            else:
                print("You can only enter 1")

    def menu():
        print("Enter 1 for tunes")
        print("Enter 2 to exit")
        choice = int(input())

        if choice == 1:
            play()
        elif choice == 2:
            print("bye")
            return choice

    while True:
        os.system("cls" if os.name == "nt" else "clear")  # The basic version doesn't work so Ai suggested this
        print("\n" * 100)  # and this

        choice = menu()
        if choice == 2:
            break
        print("")


def day_27():  # Challenge Part 1
    print()
    print("Entering Day 27")
    print("Character Generator ")

    def hitpoint():
        import random

        hp = random.randint(1, 6) * random.randint(1, 12)
        hp = hp // 2 # whole number divsion which returns only the
        hp = hp + 10
        return hp

    def power():
        import random

        pwr = random.randint(1, 6) * random.randint(1, 12)
        pwr = pwr // 2
        pwr = pwr + 12
        return pwr

    def character_genrator():
        name = input("Enter Your Character Name: ")
        title = input("Give Your Character A  Title . eg The Wise: ")
        role = input("Give your Character a role; Supporter , Attacker , Scouter , Defender :")
        print("")

        print(f"{name} {title} who is a {role}")
        print(f"HP: {hitpoint()}")  # calling the function from earlier to generate the characters stats
        print(f"HP: {power()}")

    while True:
        stop = input("Stop? ")
        if stop.lower() == "stop":
            break
        else:
            character_genrator()


def day_28():
    print()
    print("Entering Day 28")


def day_29():
    print()
    print("Entering Day 29")


def day_30():
    print()
    print("Entering Day 30")


def day_31():
    print()
    print("Entering Day 31")


def day_32():
    print()
    print("Entering Day 32")


def day_33():
    print()
    print("Entering Day 33")


def day_34():
    print()
    print("Entering Day 34")


def day_35():
    print()
    print("Entering Day 35")


def day_36():
    print()
    print("Entering Day 36")


def day_37():
    print()
    print("Entering Day 37")


def day_38():
    print()
    print("Entering Day 38")


def day_39():
    print()
    print("Entering Day 39")


def day_40():
    print()
    print("Entering Day 40")


while True:
    day = int(input("which day do you want to go to. Or Press 0 to exit: "))

    if day == 0:
        break
    elif day == 21:
        day_21()
    elif day == 22:
        day_22()
    elif day == 23:
        day_23()
    elif day == 24:
        day_24()
    elif day == 25:
        day_25()
    elif day == 26:
        day_26()
    elif day == 27:
        day_27()
    elif day == 28:
        day_28()
    elif day == 29:
        day_29()
    elif day == 30:
        day_30()
    elif day == 31:
        day_31()
    elif day == 32:
        day_32()
    elif day == 33:
        day_33()
    elif day == 34:
        day_34()
    elif day == 35:
        day_35()
    elif day == 36:
        day_36()
    elif day == 37:
        day_37()
    elif day == 38:
        day_38()
    elif day == 39:
        day_39()
    elif day == 40:
        day_40()
    else:
        print("This file only contains day 21 to 40")

print("bye")
