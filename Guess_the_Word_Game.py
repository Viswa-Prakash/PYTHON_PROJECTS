import random

def choose_word():
    word_list = ["python", "numpy", "pandas", "seaborn", "matplotlib"]
    return random.choice(word_list)

def play_game(secret_word):
    guesses_left = 10
    guessed_letters = []
    display_word = ["-"] * len(secret_word)

    while guesses_left > 0:
        print(" ".join(display_word))

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess

            if "-" not in display_word:
                print("Congratulations!, You guessed the word:", secret_word)
                break
        else:
            guesses_left -= 1
            print(f"Worng guess!, {guesses_left} guesses left")

    if guesses_left == 0:
        print(f"Sorry, You are out of guess. The word was {secret_word}")

secret_word = choose_word()
print("Welcome to Guess the Word game")
play_game(secret_word)