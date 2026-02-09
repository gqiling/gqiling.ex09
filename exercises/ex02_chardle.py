"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730662608"


def main() -> None:
    """Entry point for the Chardle game - coordinates the game flow."""
    # Call contains_char with inputs from input_word and input_letter
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Prompts user for a 5-character word and returns it."""
    word: str = input("Enter a 5-character word: ")

    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exit if not contain 5 characters

    return word


def input_letter() -> str:
    """Prompts user for a single character character word and returns it."""
    letter: str = input("Enter a single character:")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exit if not contain a single character

    return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if letter appears in word and prints matching indices."""
    print(f"Searching for {letter} in {word}")

    # Initialize counter variable to track number of matches
    count: int = 0

    # Check each index (0-4) for matches
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count = count + 1  # Increment counter when match is found

    if word[1] == letter:
        print(f"{letter} found at index 1")
        count = count + 1

    if word[2] == letter:
        print(f"{letter} found at index 2")
        count = count + 1

    if word[3] == letter:
        print(f"{letter} found at index 3")
        count = count + 1

    if word[4] == letter:
        print(f"{letter} found at index 4")
        count = count + 1

    # Print summary based on number of matches found
    if count == 0:
        print("No instances of" + letter + " found in " + word)
    elif count == 1:
        print("1 instance of" + letter + " found in " + word)
    else:
        # Note the plural 'instances' for counts > 1
        print(str(count) + " instances of" + letter + " found in " + word)


if __name__ == "__main__":
    main()
