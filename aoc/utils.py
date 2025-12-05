"""Utility functions for Advent of Code solutions."""

from pathlib import Path


def read_input(day: int, year: int, sample: bool = False) -> str:
    """Read input file for a given day.

    Args:
        day: The day number (1-25)
        sample: Whether to read the sample input
        year: The year of the puzzle (default: 2024)

    Returns:
        The contents of the input file as a string.

    Raises:
        FileNotFoundError: If the input file doesn't exist.
    """
    filename = f"day{day:02d}_sample.txt" if sample else f"day{day:02d}.txt"
    input_path = Path(__file__).parent.parent / "inputs" / f"year{year}" / filename
    return input_path.read_text().strip()


def read_lines(day: int, year: int = 2024) -> list[str]:
    """Read input file and return as list of lines.

    Args:
        day: The day number (1-25)
        year: The year of the puzzle (default: 2024)

    Returns:
        List of lines from the input file.
    """
    return read_input(day, sample=False, year=year).splitlines()


def read_ints(day: int, year: int = 2024) -> list[int]:
    """Read input file and return as list of integers.

    Args:
        day: The day number (1-25)
        year: The year of the puzzle (default: 2024)

    Returns:
        List of integers from the input file.
    """
    return [int(line) for line in read_lines(day, year)]
