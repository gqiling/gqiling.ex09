"""Mutating functions."""

__author__ = "730662607"


def manual_append(a_list: list[int], num: int) -> None:
    """Append an integer to the end of a list."""
    a_list.append(num)


def double(a_list: list[int]) -> None:
    """Multiply every element in the list by 2."""
    index: int = 0
    while index < len(a_list):
        a_list[index] = a_list[index] * 2
        index = index + 1


# Part 3: Global variables and function call
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
