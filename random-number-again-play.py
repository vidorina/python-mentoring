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
computer_number = random.randint(a=0,b=100) #random integer, so never 30.5, not floating number generator. uniform makes floating number so random.uniform(1.0, 1000.0)

attempts = 0

while True:
   attempts += 1

   my_guess = float(input("What is your guess?")) #could have used int instead of float
   if my_guess > computer_number:
       print("The number is lower than your guess")
   elif my_guess < computer_number:
       print("The number is higher than your guess")
   else:
       print(f"Congrats, you just guessed the number in {attempts} attempts! You earned a cookie. :3 You just need to buy it for yourself.")
       #A formatted string literal or f-string is a string literal that is prefixed with f or F. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
       break




#flush=True --> immediate printing! so like print("something", flush=True)

#int - not a decimal number. so like 30, without the dot.
#float - 30.5