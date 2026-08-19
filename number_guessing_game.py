import random

def main():
    """Main function to run the Number Guessing Game."""
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guesses_taken = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses_taken += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                # Correct guess!
                print(f"Good job! You guessed my number in {guesses_taken} guesses!")
                break # Exit the loop as the game is over

        except ValueError:
            print("That's not a valid number. Please enter an integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
