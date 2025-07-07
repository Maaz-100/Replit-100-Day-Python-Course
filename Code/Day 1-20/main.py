def day_1():  # basic print statements
    print()
    print("Running Day 1")
    print("""I am signing up for Replit's 100 days of Python challenge! I will make sure to spend some time every day 
    coding along, for a minimum of 10 minutes a day. I'll be using Replit, an amazing online IDE so I can do this 
    from my phone wherever I happened to be. No excuses for not coding from the middle of a field!""")
    print("i am feeling ☺️")


def day_2():  # inputs
    print()
    print("Running Day 2: ")
    name = input("what is your name: ")
    place = input("where are you: ")
    music = input("what is your favourite music: ")
    food = input("what is you favorite food ")

    print("your name is: ", name)
    print("you are probably in: ", place)
    print("your favourite music is ", music)
    print("your favourite food is ", food)


def day_3():  # Concatenate
    print()
    print("Running Day 3")

    food = input("name a food: ")
    plant = input("name a plant: ")
    cooking = input("name a cooking method: ")
    burned_food = input("name a word to describes a burnt food: ")
    item = input("name a type of household item: ")

    print("you ordered: ", cooking, " ", food, " ", burned_food, " ", item)


def day_4():  # printing in colour
    print()
    print("Running Day 4")
    name = input("What is your name?: ")
    enemy = input("What is your worst enemy's name?: ")
    power = input("What is your superpower?: ")
    location = input("Where do you live?: ")
    food = input("What is your favorite food?: ")

    print(f"Hello {name}! Your ability to \033[31m{power}\033[0m will")
    print(f"""make sure you never have to look at {enemy} again.
    Go eat {food} as you walk down the streets of {location} and use 
    {power} for good and not evil!""")


def day_5():  # if statement
    print()
    print("Running Day 5")
    print("Marvel Movie Character Creator")

    spider_man = input("Do you like 'hanging around'?: ")
    if spider_man == "yes":
        print("you're Spider-man")
    else:
        print("Then you're not Spider-man")

    korg = input("Do you have a 'gravelly' voice?: ")
    if korg == "yes":
        print("you're  Korg")
    else:
        print("Aww, then you're not Korg")

    captain_marvel = input("Do you often feel 'Marvelous'?: ")
    if captain_marvel == "yes":
        print("Aha! You're Captain Marvel! Hi!")
    else:
        print("Aha! You're not Captain Marvel! Hi!")


def day_6():  # elif
    print()
    print("Running Day 6")

    name = input("Enter your name:")
    password = input("Enter your password")

    if name == "john" and password == "1234":
        print("Welcome john hope you are well")

    elif name == "bob" and password == "0000":
        print("bob please change your password")

    else:
        print("name or password may be incorrect")


def day_7():  # nesting if statements
    print()
    print("Running Day 7")
    print("Are you a super fan of marvel")
    print("Lets find out")

    iron_man = input("Which character has an iron suit")
    if iron_man == "iron man":
        print("yes that's right")
        name = input("what was his suits assistant name: ")
        if name == "jarvis":
            print("yup that's right")
            print("you are really a super fan well done")
        else:
            print("no its called jarvis")
    else:
        print("its iron man , your a fake fan ")


def day_8():  # Challenge with everything you have learnt so far
    print()
    print("Running Day 8")
    print("Affirmation generator ")

    name = input("what is your name ? ")
    dow = input("what day is it today")

    if name == "john":
        print("whats good john")
        dow = input("what day is it? ")
        if dow == "monday":
            print("hope your feeling refreshed long a week a ahead")

        elif dow == "thursday" or "friday":
            print("The week is almost over")

        else:
            print("you can get thorough this week")

    elif name == "bob":
        print("how u doing ", name)

        if dow == "monday":
            print("working on a new client project i see , nice")

        elif dow == "friday":
            print("enjoy you day off")


def day_9():  # casting
    print()
    print("Running Day 9")
    print("Generation Generator")
    year = int(input("lets see which generation you belong to. Enter your birth year: "))

    if 1925 <= year <= 1946:
        print("you are a Traditionalist")
    elif 1947 <= year <= 1964:
        print("you are a Baby Boomer")
    elif 1965 <= year <= 1981:
        print("you are a Generation X")
    elif 1982 <= year <= 1995:
        print("you are a Millennial")
    elif 1996 <= year <= 2015:
        print("you are a Generation Z")
    else:
        print("Generation not defined in this range")


def day_10():  # basic maths
    print()
    print("Running Day 10")
    print("Bill calculator")

    total = float(input("What was the total: "))
    people = int(input("How many people: "))
    tip = float(input("what percentage would you like to give as a tip: "))
    per_person = total / people

    print("")
    print("the total is ", total)
    print("there is ", people, " people so everyone has to give: ", per_person)

    print("you wanted ", tip, "% tip so now everyone has to give and extra ", ((total * tip) / 100) / people)
    per_person = per_person + ((total * tip) / 100) / people
    print("so the total per person is: ", per_person)


def day_11():  # challenge , seconds calculator
    print()
    print("Running Day 11")
    print("how many seconds in x days")

    days = int(input("How many days do you want to calculate "))
    print(" days = ", days)
    print("meaning ", days * 24, " hours")
    print("meaning ", days * 24 * 60, " minutes")
    print("meaning ", days * 24 * 60 * 60, " seconds")


def day_12():  # debugging code
    print()
    print("Running Day 12")
    # print("100 Days of Code QUIZ")
    # print()
    # print("How many can you answer correctly?)
    # ans1 = ("What language are we writing in?")
    # if ans1 == "python":
    #   print("Correct")
    # else:
    #   print("Nope🙈
    # ans2 = input("Which lesson number is this?")
    # if(ans2>12):
    # print("We're not quite that far yet")
    # else:
    #   print("We've gone well past that!")
    # elif(ans2==12):
    #   print("That's right!")

    print("100 Days of Code QUIZ")
    print()
    print("How many can you answer correctly? ")
    ans1 = input("What language are we writing in? ")
    if ans1 == "python":
        print("Correct")
    else:
        print("Nope🙈")
    ans2 = int(input("Which lesson number is this? "))
    if ans2 > 12:
        print("We're not quite that far yet")
    elif ans2 == 12:
        print("That's right!")
    else:
        print("We've gone well past that!")


def day_13():  # Another challenge making grading tool

    print()
    print("Running Day 13")
    print("Grading tool")

    max = int(input("What was total marks on the test: "))
    score = int(input("and what did you get: "))
    grade: float = (score / max) * 100

    print("you got ", grade, "%")

    if grade >= 90:
        print("you got and A+")
    elif grade >= 80:
        print("you got a A")
    elif grade >= 70:
        print("you got a B")
    elif grade >= 60:
        print("you got a C")
    elif grade >= 50:
        print("you got a D")
    else:
        print("you got a U")


def day_14():  # rock paper scissor
    import getpass
    print()
    print("Running Day 14")
    print("Rock paper scissor ")

    player1 = getpass.getpass("Player 1, enter your move : ")  # I am using getpass as it allows the inputs to be hidden
    player2 = getpass.getpass("Player 2, enter your move : ")

    if player1 == "rock":
        if player2 == "rock":
            print("draw")

        elif player2 == "paper":
            print("Player 2 wins")

        elif player2 == "scissor":
            print("Player 1 wins")
        else:
            print("player 2 move not valid")

    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")

        elif player2 == "paper":
            print("draw")

        elif player2 == "scissor":
            print("Player 2 wins")

        else:
            print("player 2 move not valid")

    elif player1 == "scissor":
        if player2 == "rock":
            print("Player 2 wins")

        elif player2 == "paper":
            print("Player 1 wins")

        elif player2 == "scissor":
            print("draw")

        else:
            print("player 2 move not valid")
    else:
        print("player move not valid")


def day_15():  # while loops
    print()
    print("Running Day 15")
    print("animal sounds")

    while True:
        animal = input("what animal do you want to listen to today? or press 'no' to exit")
        if animal == "cow":
            print("moo")
        elif animal == "pig":
            print("oink")
        elif animal == "duck":
            print("quack")
        elif animal == "sheep":
            print("baa")
        elif animal == "no":
            break
        else:
            print("sorry, we don't have that animal")


def day_16():  # rock paper scissor with scores
    print()
    print("Running Day 16")
    print("rock paper scissor 2.0")

    print("Welcome to Name the Song Lyric")
    print()
    print("Figure out the missing word as quickly as you can!")
    print()

    counter = 1
    while True:
        lyrics = input("I don't wanna ______ a thing. ")
        if lyrics == "miss" or lyrics == "Miss":
            print("You got it!")
        else:
            print("Nope! Try again!")
            counter += 1
        if lyrics == "miss":
            break
    print("Thanks for playing!")

    print("You got the correct lyrics in", counter, "attempt(s).")


def day_17():
    import getpass
    print()
    print("Running Day 17")
    print("rock paper scissor 2.0")

    player1_score = 0
    player2_score = 0

    while True:
        player1 = getpass.getpass("Player 1, enter your move : ")
        player2 = getpass.getpass("Player 2, enter your move : ")

        if player1 == "rock":
            if player2 == "rock":
                print("draw")
                print("no points")

            elif player2 == "paper":
                print("Player 2 wins")
                player2_score += 1

            elif player2 == "scissor":
                print("Player 1 wins")
                player1_score += 1

            else:
                print("player 2 move not valid")

        elif player1 == "paper":
            if player2 == "rock":
                print("Player 1 wins")
                player1_score += 1

            elif player2 == "paper":
                print("draw")
                print("no points")

            elif player2 == "scissor":
                print("Player 2 wins")
                player2_score += 1

            else:
                print("player 2 move not valid")

        elif player1 == "scissor":
            if player2 == "rock":
                print("Player 2 wins")
                player2_score += 1

            elif player2 == "paper":
                print("Player 1 wins")
                player1_score += 1

            elif player2 == "scissor":
                print("draw")
                print("no points")

            else:
                print("player 2 move not valid")
        else:
            print("player 1 move not valid")

        if player1_score == 3:
            print("Player 1 won")
            break

        if player2_score == 3:
            print("Player 2 won")
            break


def day_18():  # feedback loops
    print()
    print("Running Day 18")
    print("Guessing game")

    to_guess = 8548411
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


def day_19():  # for loops
    print()
    print("Running Day 19")
    print("compound interest calculator")

    start_price = float(input("enter starting amount: "))
    payments = int(input("enter number of payments: "))
    apr = float(input("enter apr% "))

    for i in range(payments):
        start_price = start_price * (1 + apr / 100)
        print("Payemnt ", i, " = ", round(start_price, 2))  # round function will round to 2 decimal places


def day_20():  # understanding all parameters of the for loop
    print()
    print("Running Day 20")
    print("list Generator")

    start = int(input("what number do you want to start at"))
    end = int(input("what number do you want to go to"))
    increments = int(input("what increments do you want to go to"))

    for i in range(start, end, increments):
        print(i)


while True:
    print("")
    day = int(input("Which Day would you like to open? "))

    if day == 0:
        break
    elif day == 1:
        day_1()
    elif day == 2:
        day_2()
    elif day == 3:
        day_3()
    elif day == 4:
        day_4()
    elif day == 5:
        day_5()
    elif day == 6:
        day_6()
    elif day == 7:
        day_7()
    elif day == 8:
        day_8()
    elif day == 9:
        day_9()
    elif day == 10:
        day_10()
    elif day == 11:
        day_11()
    elif day == 12:
        day_12()
    elif day == 13:
        day_13()
    elif day == 14:
        day_14()
    elif day == 15:
        day_15()
    elif day == 16:
        day_16()
    elif day == 17:
        day_17()
    elif day == 18:
        day_18()
    elif day == 19:
        day_19()
    elif day == 20:
        day_20()
    else:
        print("Invalid day. Please enter a number between 1 and 20, or 0 to exit.")
