import random 

number_to_guess= random.randint(1,100)
guess = 0

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print ("Too low! Try again")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number: {number_to_guess}")

print("Tnank you for playing the game !")

