import random

def get_computer_choice():
    """Randomly returns 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the game's rules."""
    if user_choice == computer_choice:
        return "tie"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    
    return "computer"

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    player_score = 0
    computer_score = 0
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        try:
            wins_needed = int(input("First to how many wins? (e.g., 3): ").strip())
            if wins_needed > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while player_score < wins_needed and computer_score < wins_needed:
        print("\n-----------------------------------------")
        print(f"Score -> You: {player_score} | Computer: {computer_score}  (First to {wins_needed} wins)")
        
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
        
        if user_choice == 'quit':
            print("\nGame ended early.")
            break
            
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
            
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            print("Result: You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Result: You lose this round!")
            computer_score += 1
        else:
            print("Result: It's a tie!")
            
    # --- Announce the final winner ---
    print("\n--- Game Over! ---")
    if player_score == wins_needed:
        print(f"Congratulations! You are the champion, winning {player_score} to {computer_score}!")
    elif computer_score == wins_needed:
        print(f"Sorry, the computer is the champion, winning {computer_score} to {player_score}.")
    else:
        print("No champion was decided.")
        
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
