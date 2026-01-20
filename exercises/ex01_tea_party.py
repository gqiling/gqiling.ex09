"""Calculate the price of tea at the tea party"""

__author__ = "730662607"


def main_planner(guests: int) -> None:
    """
    Display evertyhing together
    """
    # Print the header with the number of guests
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Calculate and display tea bags needed using keyword argument
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Calculate and display treats needed using keyword argument
    print("Treats: " + str(treats(people=guests)))
    # Calculate total cost by calling tea_bags and treats again
    # Need to call both functions to get their values for cost calculation
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """
    Calculate the number of tea bags needed for a tea party.
    Each guest is expected to drink two cups of tea.
    """
    # Each person drinks 2 cups of tea, so multiply people by 2
    return people * 2


def treats(people: int) -> int:
    """
    Compute the number of treats needed based on the number of teas.
    each tea a guest drinks needs 1.5 treats to accompany it.
    """
    # First get the number of teas by calling tea_bags with keyword argument
    # Then multiply by 1.5 (treats per tea) and convert to int
    # Used int() because we can't have partial treats, and return type must be int
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    compute the cost of the tea bags and the treats combined
    tea bag costs $0.50 and each treat costs $0.75
    """
    # Calculate total: (tea bags * $0.50) + (treats * $0.75)
    # Returns a float to handle decimal dollar amounts
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
