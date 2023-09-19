import random

def main():
    # Generate a random number between 0 and 100
    secret_number = random.randint(0, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 100.")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number between 0 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Higher! Try again.")
        elif guess > secret_number:
            print("Lower! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
