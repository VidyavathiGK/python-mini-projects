import random

def get_computer_choice():
    """Randomly returns 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the game's rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Winning combinations for the user
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    
    # If it's not a tie and the user didn't win, the computer must have won
    return "You lose!"

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    player_score = 0
    computer_score = 0
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        print("\n-----------------------------------------")
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
        
        if user_choice == 'quit':
            print("\n--- Final Score ---")
            print(f"You: {player_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break
            
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
            
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")
        
        # Update the score
        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1
            
        print(f"Score -> You: {player_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
