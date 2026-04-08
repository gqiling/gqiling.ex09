"""Point class with mutating and non-mutating scale methods."""

from __future__ import annotations  # allows Point to return its own type

__author__ = "730662607"


class Point:
    """Represents a point on an (x, y) coordinate graph."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initialize a Point with x and y coordinates."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutate this Point by multiplying x and y by factor."""
        # Directly update x and y on THIS point (mutates the original)
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Return a NEW Point with x and y multiplied by factor.

        The original Point is NOT changed.
        """
        # Create and return a brand new Point — does not touch self.x or self.y
        return Point(self.x * factor, self.y * factor)
