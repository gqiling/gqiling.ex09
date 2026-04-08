"""Utility functions for working with dictionaries."""

__author__ = "730662607"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    # Start with an empty dictionary to store the inverted result
    result: dict[str, str] = {}

    # Loop through every key in the input dictionary
    for key in input:
        # Get the value associated with the current key
        value = input[key]

        # If the value already exists as a key in result, we have a duplicate
        # Keys must be unique, so raise a KeyError to signal the problem
        if value in result:
            raise KeyError("Duplicate key encountered during inversion!")

        # Otherwise, flip it: the old value becomes the key, old key becomes value
        result[value] = key

    return result


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Return the most frequently appearing color in the dictionary.

    In the case of a tie, return the color that appeared first.
    """
    # Build a frequency count of how many times each color appears
    color_counts: dict[str, int] = {}
    for name in names_and_colors:
        color = names_and_colors[name]  # Get the color for this person
        if color in color_counts:
            # Color already seen before — increment its count
            color_counts[color] += 1
        else:
            # First time seeing this color — initialize its count to 1
            color_counts[color] = 1

    # Now find which color has the highest count
    most_popular: str = ""
    highest_count: int = 0
    for color in color_counts:
        # Only update if strictly greater, so the first color seen wins any tie
        if color_counts[color] > highest_count:
            highest_count = color_counts[color]
            most_popular = color

    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Count the frequency of each item in a list."""
    # Start with an empty dictionary to accumulate counts
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            # Item already has a count — add 1 to it
            result[item] += 1
        else:
            # First time seeing this item — start its count at 1
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorize words into a dictionary by their starting letter.

    Words that do not start with an alphabetic character are ignored.
    """
    # Start with an empty dictionary to store letter -> word list pairs
    result: dict[str, list[str]] = {}

    for word in words:
        # Only process the word if its first character is a letter
        # This skips things like "#COMP110" which start with a symbol
        if word[0].isalpha():
            # Use lowercase version of the first letter as the key
            # so "Hello" and "hello" both go under 'h'
            letter = word[0].lower()

            if letter in result:
                # Letter already exists — append the word to its list
                result[letter].append(word)
            else:
                # First word for this letter — create a new list
                result[letter] = [word]

    return result


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Mutate the attendance log by adding a student to the given day."""
    if day in log:
        # Day already exists in the log — just append the new student
        log[day].append(student)
    else:
        # Day not yet in the log — create a new entry with this student
        log[day] = [student]

    # No return value — this function mutates the dictionary directly
