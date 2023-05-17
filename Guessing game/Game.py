import random

number = random.randint(1, 10)

name = input("Hello, What's your name? ")

print(f"Hey, {name} you are Guessing a number between 1 and 10: ")

guese = True
tries = 5
turns = 1

while guese == True and turns < tries:
    inp = int(input("Your guese: "))
    if inp == number:
        print(f"You guesed the number in {turns} tries")
        guese = guese + 1
        guese = False
    elif inp < number:
        print("Your guess is too low")
        turns = turns + 1
    else:
        print("Your guese is to high")
        turns = turns + 1