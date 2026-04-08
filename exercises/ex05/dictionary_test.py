"""Unit tests for the dictionary utility functions in dictionary.py."""

__author__ = "730662607"

import pytest
from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


# =============================================================================
# Tests for invert
# =============================================================================


def test_invert_simple_three_pairs() -> None:
    """Test inverting a dictionary with three unique key-value pairs."""
    # Standard use case: every key and value is unique
    input_dict = {"a": "z", "b": "y", "c": "x"}
    result = invert(input_dict)
    assert result == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair() -> None:
    """Test inverting a dictionary with only one key-value pair."""
    # Use case: smallest possible non-empty dictionary
    input_dict = {"apple": "cat"}
    result = invert(input_dict)
    assert result == {"cat": "apple"}


def test_invert_raises_key_error_on_duplicate_values() -> None:
    """Edge case: inverting should raise KeyError when two keys share the same value."""
    # Duplicate values would create duplicate keys after inversion — must raise KeyError
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_invert_empty_dictionary() -> None:
    """Edge case: inverting an empty dictionary should return an empty dictionary."""
    result = invert({})
    assert result == {}


# =============================================================================
# Tests for favorite_color
# =============================================================================


def test_favorite_color_clear_winner() -> None:
    """Test that the color appearing most frequently is returned."""
    # Use case: 'blue' appears twice, 'yellow' once — blue should win
    names_colors = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    result = favorite_color(names_colors)
    assert result == "blue"


def test_favorite_color_single_entry() -> None:
    """Test with only one person — their color must be the favorite."""
    # Use case: only one person, trivially their color is the most popular
    names_colors = {"Alice": "green"}
    result = favorite_color(names_colors)
    assert result == "green"


def test_favorite_color_tie_returns_first() -> None:
    """Edge case: when two colors tie, return the one that appeared first."""
    # 'red' and 'blue' each appear once — 'red' appears first in the dictionary
    names_colors = {"Alice": "red", "Bob": "blue"}
    result = favorite_color(names_colors)
    assert result == "red"


def test_favorite_color_all_same() -> None:
    """Edge case: when all people share the same color, that color is returned."""
    names_colors = {"Alice": "purple", "Bob": "purple", "Carol": "purple"}
    result = favorite_color(names_colors)
    assert result == "purple"


# =============================================================================
# Tests for count
# =============================================================================


def test_count_multiple_items() -> None:
    """Test counting a list with repeated items."""
    # Use case: 'a' appears 3 times, 'b' appears 2 times
    result = count(["a", "b", "a", "a", "b"])
    assert result == {"a": 3, "b": 2}


def test_count_all_unique() -> None:
    """Test counting a list where every item is unique."""
    # Use case: each item appears exactly once
    result = count(["cat", "dog", "fish"])
    assert result == {"cat": 1, "dog": 1, "fish": 1}


def test_count_empty_list() -> None:
    """Edge case: counting an empty list should return an empty dictionary."""
    result = count([])
    assert result == {}


def test_count_single_item_repeated() -> None:
    """Edge case: a list with only one unique value repeated many times."""
    result = count(["x", "x", "x", "x"])
    assert result == {"x": 4}


# =============================================================================
# Tests for alphabetizer
# =============================================================================


def test_alphabetizer_basic_grouping() -> None:
    """Test that words are correctly grouped by their first letter."""
    # Use case: standard grouping of words starting with different letters
    result = alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"])
    assert result == {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "bad"]}


def test_alphabetizer_case_insensitive_key() -> None:
    """Test that uppercase and lowercase words are grouped under the same key."""
    # Use case: 'Python' and 'party' should both go under 'p'
    result = alphabetizer(["Python", "sugar", "Turtle", "party", "table"])
    assert result == {
        "p": ["Python", "party"],
        "s": ["sugar"],
        "t": ["Turtle", "table"],
    }


def test_alphabetizer_skips_non_alpha() -> None:
    """Edge case: words starting with non-alphabetic characters should be ignored."""
    # '#COMP110' starts with '#' — should not appear in result
    result = alphabetizer(["Hello", "#COMP110", "hello"])
    assert result == {"h": ["Hello", "hello"]}


def test_alphabetizer_empty_list() -> None:
    """Edge case: an empty list should return an empty dictionary."""
    result = alphabetizer([])
    assert result == {}


# =============================================================================
# Tests for update_attendance
# =============================================================================


def test_update_attendance_add_to_existing_day() -> None:
    """Test adding a student to a day that already exists in the log."""
    # Use case: Tuesday already exists, Vrinda is added to it
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(log, "Tuesday", "Vrinda")
    assert log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}


def test_update_attendance_add_new_day() -> None:
    """Test adding a student on a day that does not yet exist in the log."""
    # Use case: Wednesday is a new day — should be created with Kaleb
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(log, "Wednesday", "Kaleb")
    assert log == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa"],
        "Wednesday": ["Kaleb"],
    }


def test_update_attendance_returns_none() -> None:
    """Test that update_attendance returns None (it mutates, does not return)."""
    # update_attendance should mutate in place and return None
    log: dict[str, list[str]] = {"Monday": ["Alice"]}
    result = update_attendance(log, "Monday", "Bob")
    assert result is None


def test_update_attendance_empty_log() -> None:
    """Edge case: updating an empty log should create the first entry."""
    log: dict[str, list[str]] = {}
    update_attendance(log, "Friday", "Sam")
    assert log == {"Friday": ["Sam"]}
