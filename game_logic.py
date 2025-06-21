import random
import ascii_art
WORDS = ["python", "git", "github", "snowman", "meltdown"]
def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    max_mistakes = len(ascii_art.STAGES) - 1
    print("Welcome to Snowman Meltdown!")
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single **letter** (a-z).")
            continue
            guessed_letters.append(guess)
        if guess in secret_word:
           print("Correct guess!")
        else:
          mistakes += 1
          print("Wrong guess! The snowman is melting...")
        # Check for win
        if all(letter in guessed_letters for letter in secret_word):
           display_game_state(mistakes, secret_word, guessed_letters)
           print(f" You saved the snowman! The word was '{secret_word}'.")
           break
        # Check for loss
        if mistakes >= max_mistakes:
           display_game_state(mistakes, secret_word, guessed_letters)
           print(f"The snowman melted! The word was '{secret_word}'.")
           break
        # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing Snowman Meltdown! Stay cool.")


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print("\n" + "=" * 40)
    print(ascii_art.STAGES[mistakes])
    print("-" * 40)
    # Build a display version of the secret word.
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word:           {display_word}")
    print(f"Mistakes:       {mistakes}/{len(ascii_art.STAGES) - 1}")
    print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
    print("=" * 40 + "\n")
