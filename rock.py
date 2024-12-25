import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Options: \n1. Rock\n2. Paper\n3. Scissors")

    # User input
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().lower()

    # Validating user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return

    # Computer's random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice.capitalize()}")

    # Determine the winner using conditional statements
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You win!")
    else:
        print("You lose! Better luck next time.")

if __name__ == "__main__":
    play_game()
