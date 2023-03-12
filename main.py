import random

# Initialize the level dictionary
level_dict = {"k": (1, 50, 20), "s": (1, 100, 15), "n": (1, 150, 10)}

# Ask the user to select a level
level = input("Select a level (K for easy, S for medium, N for hard): ").lower()

# Check if the level is valid
if level not in level_dict:
    print("Invalid level!")
    exit()

# Get the minimum, maximum values, and number of guesses for the selected level
min_val, max_val, num_guesses = level_dict[level]

# Ask the user to input the number of rounds
num_rounds = int(input("Enter the number of rounds: "))

# Initialize the scores
user_score = 0
machine_score = 0

# Loop for the number of rounds
for i in range(num_rounds):
    # Generate a random number between the minimum and maximum values
    number = random.randint(min_val, max_val)

    # Initialize the guess variable to 0
    guess = 0

    # Loop until the guess matches the number or the user runs out of guesses
    for j in range(num_guesses):
        # Ask the user to input a guess
        guess = int(input(f"Round {i+1}/{num_rounds}, guess a number between {min_val} and {max_val} (you have {num_guesses-j} guesses left): "))

        # Check if the guess is too low or too high
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            user_score += 1
            break
    else:
        print(f"Game over! The number was {number}.")
        machine_score += 1

# Print the final result
print(f"Final result: User score: {user_score}, Machine score: {machine_score}")
