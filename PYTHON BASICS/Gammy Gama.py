import random

number = random.randint(1,10)
tries = 1

username = input("Hello, What is your username? ")

print("Hello, " + username + ".")

question = input("Would you like to play a game? [Y/N]")
if question == "n":
    print("Oh!... Okay")
else:
    print("I am thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess Lower")
    elif guess < number:
        print("Guess Too Low")
    else:
        print("Correct Guess!")
    while guess != number:
        tries += 1
        guess = int(input("Try again"))
        if guess < number:
            print("Guess Higher")
    if guess == number:
        print("Great! You guessed right! The number was ", number, "and you tried ",  tries, " times")
