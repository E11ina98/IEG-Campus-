import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return choices[random.randint(1, 3) - 1]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Start with user input
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
if user_choice not in ['Rock', 'Paper', 'Scissors']:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
