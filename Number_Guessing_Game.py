import random

def number_guessing_game():
    target_number = random.randint(1,100)
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 to 100: "))
        attempts +=1

        if user_guess > target_number:
            print("Guessed number is too high")
        
        elif user_guess < target_number:
            print("Guessed number is too low")

        else:
            print(f"Congratualation! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()
    