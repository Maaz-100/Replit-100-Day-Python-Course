import time


def day_21():  # for loop + maths skills
    print()
    print("Entering Day 21")
    print("Multiplication tables")

    table = int(input("Enter the number you wanted to be tested on: "))
    end = int(input("Enter how many questions do you want : "))
    limit = end
    end = (table * end) + table
    correct = 0
    j = 0  # made j as another counter to show multiplier

    for i in range(0, end, table):
        ans = int(input(
            f"What is {table} x {j}  = "))  # using f strings as normal strings won't support variable in input lines
        if ans == i:
            print("Correct")
            print("")
            correct += 1
        else:
            print("Wrong correct answer is ", i)
        j += 1

    print(f"you got {correct} out of {limit - 1} ")  # starting to like F strings may use them more


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
        hp = hp // 2  # whole number division which returns only the
        hp = hp + 10
        return hp

    def power():
        import random

        pwr = random.randint(1, 6) * random.randint(1, 12)
        pwr = pwr // 2
        pwr = pwr + 12
        return pwr

    def character_generator():
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
            character_generator()


def day_28():  # Challenge Part 2
    print()
    print("Entering Day 28")
    print("Character Game ")

    def hitpoint():
        import random

        hp = random.randint(1, 6) * random.randint(1, 12)
        hp = hp // 2  # whole number division which returns only the
        hp = hp + 10
        return hp

    def power():
        import random

        pwr = random.randint(1, 6) * random.randint(1, 12)
        pwr = pwr // 2
        pwr = pwr + 12
        return pwr

    def character_generator_1():
        name_1 = input("Enter Your Character 1 Name: ")
        title_1 = input("Give Your Character A  Title, The Wise: ")
        role_1 = input("Give your Character a role; Supporter , Attacker , Scouter , Defender :")
        print("")

        hitpoint_1 = hitpoint()
        power_1 = power()
        print(f"{name_1} {title_1} who is a {role_1}")
        print(f"HP: {hitpoint_1}")  # calling the function from earlier to generate the characters stats
        print(f"Attack: {power_1}")
        print()

        return name_1, title_1, role_1, hitpoint_1, power_1

    def character_generator_2():
        name_2 = input("Enter Your Character 2 Name: ")
        title_2 = input("Give Your Character A  Title, eg The Wise: ")
        role_2 = input("Give your Character a role; Supporter , Attacker , Scouter , Defender :")
        print("")

        hitpoint_2 = hitpoint()
        power_2 = power()
        print(f"{name_2} {title_2} who is a {role_2}")
        print(f"HP: {hitpoint_2}")  # calling the function from earlier to generate the characters stats
        print(f"Attack: {power_2}")
        print()

        return name_2, title_2, role_2, hitpoint_2, power_2

    name_1, title_1, role_1, hitpoint_1, power_1 = character_generator_1()
    name_2, title_2, role_2, hitpoint_2, power_2 = character_generator_2()

    print("The battle starts")

    while True:
        print()
        hitpoint_1 = hitpoint_1 - power_2
        hitpoint_2 = hitpoint_2 - power_1

        print(f"{name_1} does {power_1}damage")
        print(f"{name_2} does {power_2}damage")
        print("")

        time.sleep(2)

        print(f"{name_1} has {hitpoint_1} HP left")
        print(f"{name_2} has {hitpoint_2} HP left")
        print("")

        time.sleep(1)

        if hitpoint_1 <= 0 and hitpoint_2 > 0:
            print(f"Game Over {name_2} {title_2} wins ")
            print(f"{name_2} had {hitpoint_2} left")
            print()
            break

        elif hitpoint_1 > 0 and hitpoint_2 <= 0:
            print(f"Game Over {name_1} {title_1} wins ")
            print(f"{name_1} had {hitpoint_1} left")
            print()
            break

        elif hitpoint_1 <= 0 and hitpoint_2 <= 0:
            print(f"Game Over {name_1} {title_1}; And {name_2} {title_2} draws ")
            print(f"They both killed each other at the same time ")
            print()
            break

        print("The battle continues")


def day_29():  # adding commands to print statements
    print()
    print("Entering Day 29")

    # for i in range(0, 100):
    # print(i, end=" ")

    # you can also do end="\n" to make it print on a new line.
    # you can also do end="\t" to make it print with a tab.
    # you  can also do end "\v" to print with a vertical tab.

    # also, if you want to turn the cursor on you can do print('\033[?25l', end="").
    # and for cursor off you can do print('\033[?25h', end="").

    print("Colour changing text")

    def choose_colour():
        colour = input("What colour would you like to choose? ")
        return colour

    colour = choose_colour()

    def output():
        text = input("What text would you like to display? ")
        return text

    text = output()
    while True:
        if colour == "black":
            print('\033[30m', text, '\033[0m', sep="", end="")
            print()
            break

        elif colour.lower() == "red":
            print('\033[31m', text, '\033[0m', sep="", end="")
            print()
            break

        elif colour.lower() == "green":
            print('\033[32m', text, '\033[0m', sep="", end="")
            print()
            break

        elif colour.lower() == "brown":
            print('\033[33m', text, '\033[0m', sep="", end="")
            print()
            break

        elif colour.lower() == "blue":
            print('\033[34m', text, '\033[0m', sep="", end="")
            print()
            break

        else:
            print("Sorry, I did not account for that colour")
            break


def day_30():  # F strings
    print()
    print("Entering Day 30")

    # you can do f" {variable: alignment  symbol , then number of characters to use}"

    # to right align use > and to left align use < and to center use ^

    # f{var: <3} left align with 3 spaces

    print("Feedback form")

    for i in range(1, 30):
        feedback = input(f"Enter your feedback for day {i}: ")
        print(f"Day {i} feedback you said it was")
        print(f"{feedback: ^20}")
        print("")


def day_31():  # Mock up of a GUI
    print()
    print("Entering Day 31")
    print("GUI app")

    play = "Play"
    pause = "Pause"
    new = "Next"

    print("\033[34m=== Music App ===\033[0m", end="\n")

    print(f"{play:<35}")
    print(f"{pause:^35}")
    print(f"{new:>35}")


def day_32():  #list
    import random
    print()
    print("Entering Day 32")
    print("Random Greetings")

    greetings = ["Hello", "Hola", "Bonjour", "Ciao", "Hallo", "Salam", "Namaste", "Konnichiwa", "Zdravstvuyte", "Annyeonghaseyo"]

    print(greetings[random.randint(0, len(greetings) - 1)]) # printing a random greeting by using random.randint


def day_33():
    print()
    print("Entering Day 33")
    print("To Do App")

    to_do = []

    while True:
        choice = input("Type Add or Remove or Exit: ")

        if choice.lower() == "add":
            to_do.append(input("Enter something to Add: "))
            print("")

        elif choice.lower() == "remove":
            to_do.remove(input("Enter something to Remove: "))
            print("")

        elif choice.lower() == "exit":
            break

        else:
           print("Invalid choice")
           continue

        print("To do ")
        for tasks in to_do:
            print(tasks)
        print("")

    print("bye")



def day_34():
    import time
    print()
    print("Entering Day 34")
    print("fake emails Spammer")

    fake_emails = []

    def menu():
        print("1 = Add email")
        print("2 = Remove email")
        print("3 = Spam")
        print("4 = Exit")


        choice = int(input("Where would you like go? "))
        print()

        return choice

    def add():
        fake_emails.append(input("Enter email to Add: "))
        print("")
        print("New list of emails")
        for email in fake_emails:
            print(email)
        print()

    def remove():
        fake_emails.remove(input("Enter email to Remove: "))
        print("New list of emails")
        for email in fake_emails:
            print(email)
        print()

    def spam():
        print()

        for email in fake_emails: # prints every email in a new line
            print("hello ", email)
            print("it has come to our attention that you're missing out on the")
            print("amazing Replit 100 days of code. We insist you do it right away.")
            print("If you don't we will pass on your email address to every spammer we've")
            print("ever encountered and also sign you up to the My Little Pony newsletter,")
            print("because that's neat. We might just do that anyway.") # the prompt i was told to use , plz dont judge me
            time.sleep(1)
            print()

    def leave():
        print("Thank you for using my app")


    while True:
        choice = menu()
        if choice == 1:
            add()
        elif choice == 2:
            remove()
        elif choice == 3:
            spam()
        elif choice ==4:
            leave()
            break
        else:
            print("not a valid choice")

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
    day = int(input("Which day do you want to go to. Or Press 0 to exit: "))

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
