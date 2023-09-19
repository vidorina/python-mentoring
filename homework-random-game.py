"""
guess a number:
0-100 by pc, random
not number: what I guessed is higher/lower than pc's
guess correct: program ends with you won message
infinite loop, check user input: lower, higher, same number
infinite loop ends when numbers match
"""
print("I thought of a number from 0 to 100 but it is a secret. Your job is to guess the number. I will give you hints though, because I am nice. :3")
import random
computer_number = random.randint(a=0,b=100)
my_guess = float(input("What is your guess?"))
while True:
    if my_guess > computer_number:
        print("The number is smaller than your guess")
        my_guess = float(input("What is your guess?"))
    if my_guess < computer_number:
        print("The number is greater than your guess")
        my_guess = float(input("What is your guess?"))
    if my_guess == computer_number:
        print("Congrats, you just guessed the number! You earned a cookie. :3 You just need to buy it for yourself.")
        break


    # magic. guess, store, check, status, repeat until matches.
    # integer (transform string to number), <>=
    # ctrl then / (above numpad) for bulk commenting out
    # askchatgpt

