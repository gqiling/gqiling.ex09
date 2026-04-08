"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730662607"


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        self.fish = [f for f in self.fish if f.age <= 3]
        self.bears = [b for b in self.bears if b.age <= 5]
        return None

    def remove_fish(self, amount: int):
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        self.bears = [b for b in self.bears if b.hunger_score >= 0]
        return None

    def repopulate_fish(self):
        new_fish = int(len(self.fish) / 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        new_bears = int(len(self.bears) / 2)
        for _ in range(new_bears):
            self.bears.append(Bear())
        return None

    def __str__(self) -> str:
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, r: River) -> River:
        return River(len(self.fish) + len(r.fish), len(self.bears) + len(r.bears))
        return self

    def __mul__(self, factor: int) -> River:
        return River(len(self.fish) * factor, len(self.bears) * factor)
        return self

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()
