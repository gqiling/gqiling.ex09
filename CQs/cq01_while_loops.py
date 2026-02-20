"""CQ01 - while loope."""

__author__ = "730662608"


def num_instances(phrase: str, search_char: str) -> int:
    """Count the number of times search_char appears in phrase."""
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1

    return count


def get_evens(numbers: str) -> str:
    """Return a string containing only the even digits from numbers."""
    evens: str = ""
    index: int = 0

    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            evens = evens + numbers[index]
        index = index + 1

    return evens
