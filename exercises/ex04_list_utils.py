"""Utility functions for working with lists."""

__author__ = "730662607"


def all(input: list[int], value: int) -> bool:
    """Return True if every element in the list matches the given value."""
    # If the list is empty, return False — nothing to match
    if len(input) == 0:
        return False

    # Loop through each number in the list
    for num in input:
        # If any number does NOT match the given value, we can stop immediately
        # and return False — no need to check the rest
        if num != value:
            return False

    # If we made it through the entire loop without returning,
    # then every element matched — return True
    return True


def max(input: list[int]) -> int:
    """Return the largest integer in the list.

    Raises a ValueError if the list is empty.
    """
    # Cannot find a max of an empty list — raise an error right away
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # Assume the first element is the largest to start
    largest: int = input[0]

    # Loop through the rest of the list starting at index 1
    i: int = 1
    while i < len(input):
        # If the current element is bigger than our current largest, update it
        if input[i] > largest:
            largest = input[i]
        i += 1  # Move to the next index

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if both lists have the same elements at every index."""
    # If the lists have different lengths, they cannot be equal
    if len(list1) != len(list2):
        return False

    # Loop through each index and compare the elements one by one
    i: int = 0
    while i < len(list1):
        # If any pair of elements at the same index differs, they are not equal
        if list1[i] != list2[i]:
            return False
        i += 1  # Move to the next index

    # Made it through every index without a mismatch — the lists are equal
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate list1 by appending all elements of list2 to the end of it."""
    # Loop through every element in list2
    i: int = 0
    while i < len(list2):
        # Append the current element of list2 onto the end of list1
        list1.append(list2[i])
        i += 1  # Move to the next index

    # No return value — list1 has been mutated directly
