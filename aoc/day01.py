"""Day 01: Template

This is a template for solving Advent of Code puzzles.
Copy this file and rename it for each day's solution.
"""


def parse_input(data: str) -> list[str]:
    """Parse the input data.

    Args:
        data: Raw input string

    Returns:
        Parsed data structure
    """
    return data.strip().splitlines()


def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 1
    """
    parsed = parse_input(data)
    # TODO: Implement solution
    return 0


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)
    # TODO: Implement solution
    return 0


if __name__ == "__main__":
    from aoc.utils import read_input

    data = read_input(1)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
