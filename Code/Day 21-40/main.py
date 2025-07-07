def day_21():  # for loop + maths skills
    print()
    print("Entering Day 21")
    print("Multiplication tables") 

    
    table = int(input("Enter the number you wanted to be tested on: "))
    end = int(input("Enter how many questions do you want : "))
    end = (table*end)+table
    correct = 0
    j = 0 # made j as another counter to show multipler

    for i in range(0,end,table):
        ans = int(input(f"what is {table} x {j}  = " )) # using f strings as normal strings wont support variable in input lines 
        if ans == i:
            print("Correct")
            print("")
            correct +=1
        else:
            print("Wrong correct answer is " , i)
        j+=1

    print(f"you got  {correct}") #starting to like F strings may use them more 


def day_22(): # starting to use libraries 
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



def day_23(): # subroutines
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

def day_24():
    print()
    print("Entering Day 24")


def day_25():
    print()
    print("Entering Day 25")


def day_26():
    print()
    print("Entering Day 26")


def day_27():
    print()
    print("Entering Day 27")


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
        print("This file only contains day 21 to 40" )

print("bye")

