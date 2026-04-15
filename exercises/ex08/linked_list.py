"""Linked list recursive algorithms for exercises."""

from __future__ import annotations


class Node:
    """A node in a singly linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a node with a value and a reference to the next node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Return a string representation of the linked list starting at this node."""
        return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return value of node at given index."""
    # Edge case: empty list
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    # Base case
    if index == 0:
        return head.value

    # Recursive case
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")

    # Base case: last node
    if head.next is None:
        return head.value

    # Recursive case
    rest_max = max(head.next)

    if head.value > rest_max:
        return head.value
    else:
        return rest_max


def linkify(items: list[int]) -> Node | None:
    """Convert Python list to linked list."""
    # Base case
    if len(items) == 0:
        return None

    # Recursive case
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return new linked list with values scaled by factor."""
    # Base case
    if head is None:
        return None

    # Recursive case
    return Node(head.value * factor, scale(head.next, factor))
