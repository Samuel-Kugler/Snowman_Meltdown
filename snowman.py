import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def user_input(guessed_letters: str) -> str:
    """
    Gets one letter from the user and checks that it wasn't guessed before.
    :param guessed_letters: str
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if not guess.isalpha() or not len(guess) == 1:
            print(f"{guess} is not a valid input! "
                  f"A valid input must be 1 letter only!")
            continue

        if guess in guessed_letters:
            print(f"{guess} was already tried! Try a different letter!")
            continue

        return guess


def right_guess(guess: str, secret_word: str) -> bool:
    """
    Checks if the user guessed right.
    :param guess: str
    :param secret_word:
    :return: bool
    """
    return guess in secret_word


def get_game_guess_state(secret_word: str, guessed_letters: str) -> str:
    """
    Returns the current stage of the word.
    :param secret_word: str
    :param guessed_letters: str
    :return: str
    """
    result = ""

    for letter in secret_word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"

    return result


def display_game_state(mistakes: int, secret_word: str, guessed_letters: str):
    """
    Displays the complete game state.
    :param mistakes: int
    :param secret_word: str
    :param guessed_letters: str
    """
    current_word = get_game_guess_state(secret_word, guessed_letters)

    #printing snowman
    print(STAGES[mistakes])

    #printing guessing progress
    print(" " * 5 + current_word + "\n")


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    mistakes = 0
    max_mistakes = len(STAGES) - 1
    guessed_letters = ""

    #starting snowman
    print(STAGES[mistakes])

    while mistakes < max_mistakes:
        #valid guess
        guess = user_input(guessed_letters)
        guessed_letters = guessed_letters + guess

        #display current snowman and guess
        if not right_guess(guess, secret_word):
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)

    #user finish
    if mistakes == max_mistakes:
        print("The poor snowman melted...")
    else:
        print("Congratz! You saved the snowman!")


if __name__ == "__main__":
    play_game()
