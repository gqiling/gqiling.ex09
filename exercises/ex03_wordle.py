"""ex03 - wordle."""

__author__ = "730662608"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user for a guess and ensure it matches the secret word length."""
    # Get initial guess from user
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    # Keep prompting until guess is correct length
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if char_guess appears anywhere in secret_word."""
    # Ensure char_guess is exactly one character
    assert len(char_guess) == 1

    index: int = 0

    # Check each character in secret_word
    while index < len(secret_word):
        # If match found, return True immediately
        if secret_word[index] == char_guess:
            return True
        index = index + 1

    # No match found after checking all characters
    return False


def emojified(guess: str, secret: str) -> str:
    """Return emojis representing the accuracy of the guess compared to word."""
    # Ensure both strings are same length
    assert len(guess) == len(secret)

    # Define emoji constants
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"

    result: str = ""
    index: int = 0

    # Check each character position
    while index < len(guess):
        # Green: correct character in correct position
        if guess[index] == secret[index]:
            result = result + GREEN_BOX
        # Yellow: correct character in wrong position
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            result = result + YELLOW_BOX
        # White: character not in secret word
        else:
            result = result + WHITE_BOX
        index = index + 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Initialize game state variables
    turn: int = 1
    max_turns: int = 6
    won: bool = False

    # Game loop: continue while turns remain and player hasn't won
    while turn <= max_turns and not won:
        # Display current turn
        print(f"=== Turn {turn}/{max_turns} ===")

        # Get valid guess from user
        guess: str = input_guess(secret_word_len=len(secret))

        # Show emoji feedback
        result: str = emojified(guess=guess, secret=secret)
        print(result)

        # Check if player won
        if guess == secret:
            won = True
        else:
            # Move to next turn if guess was wrong
            turn = turn + 1

    # Display end game message
    if won:
        print(f"You won in {turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
