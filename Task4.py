import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0


def get_computer_choice():
    return random.choice(choices)


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "scissors" and computer == "paper")
        or (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"


def play_game():
    global user_score, computer_score

    print("\n===== ROCK-PAPER-SCISSORS GAME =====")
    print("Choices: rock, paper, scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        return

    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")


# Main loop
while True:
    play_game()

    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("\nThanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
