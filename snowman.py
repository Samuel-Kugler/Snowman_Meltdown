import game_logic as game
from Snowman_Meltdown.game_logic import user_input

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def main():
    #first run
    game.play_game()

    #more runs
    while True:
        user_choice = input("Do you want to play another round?(yes/no)").strip()

        if user_choice == "no":
            break
        elif user_choice == "yes":
            game.play_game()
        else:
            print("Invalid input, please enter either yes or no!")


if __name__ == "__main__":
    main()
