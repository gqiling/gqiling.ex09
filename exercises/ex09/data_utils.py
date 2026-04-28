"""Data related utility functions."""

__author__ = "730662607"

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted


"""These are the functions we wrote/will write in class!"""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


# ── NEW PART 0 FUNCTIONS ──────────────────────────────────────────────────────


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Return the first `num_rows` rows of a column-oriented table.

    If `num_rows` is greater than or equal to the number of rows in the table,
    the entire table is returned unchanged.

    Args:
        table:    A column-oriented data table (output of columnar).
        num_rows: How many rows from the top to keep.

    Returns:
        A new column-oriented table containing only the first `num_rows` rows.

    Example:
        >>> t = {"a": ["1", "2", "3"], "b": ["x", "y", "z"]}
        >>> head(t, 2)
        {"a": ["1", "2"], "b": ["x", "y"]}
    """
    result: dict[str, list[str]] = {}

    for col in table:
        result[col] = table[col][:num_rows]

    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Return a new table containing only the specified columns.

    Args:
        table:   A column-oriented data table.
        columns: A list of column names (keys) to keep.

    Returns:
        A new column-oriented table with only the requested columns,
        in the order given by `columns`.

    Example:
        >>> t = {"a": ["1", "2"], "b": ["x", "y"], "c": ["p", "q"]}
        >>> select(t, ["a", "c"])
        {"a": ["1", "2"], "c": ["p", "q"]}
    """
    result: dict[str, list[str]] = {}

    for col in columns:
        result[col] = table[col]

    return result


def concat(
    first: dict[str, list[str]], second: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Concatenate two column-oriented tables that share the same columns.

    Appends all rows of `second` after all rows of `first`. Both tables must
    have exactly the same set of column names.

    Args:
        first:  A column-oriented data table.
        second: A column-oriented data table with the same columns as `first`.

    Returns:
        A new column-oriented table with all rows from `first` followed by
        all rows from `second`.

    Example:
        >>> a = {"x": ["1", "2"], "y": ["a", "b"]}
        >>> b = {"x": ["3"],      "y": ["c"]}
        >>> concat(a, b)
        {"x": ["1", "2", "3"], "y": ["a", "b", "c"]}
    """
    result: dict[str, list[str]] = {}

    for col in first:
        result[col] = first[col] + second[col]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the frequency of each unique value in a list of strings.

    Args:
        values: A list of string values (typically one column from a table).

    Returns:
        A dict mapping each unique value to the number of times it appears.
        Empty strings are counted like any other value.

    Example:
        >>> count(["a", "b", "a", "c", "b", "a"])
        {"a": 3, "b": 2, "c": 1}
    """
    result: dict[str, int] = {}

    for val in values:
        if val in result:
            result[val] += 1
        else:
            result[val] = 1

    return result
