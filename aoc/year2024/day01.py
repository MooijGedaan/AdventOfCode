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
    
    # Set up the two arrays
    arr1 = []
    arr2 = []

    for line in parsed:
        arr1.append(line.split(" ")[0])
        arr2.append(line.split(" ")[3])

    # Sort them
    arr1.sort()
    arr2.sort()

    total_distance = 0

    # Calculate difference
    for i, _ in enumerate(arr1):
        total_distance += abs(int(arr1[i]) - int(arr2[i]))

    return total_distance


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)

        # Set up the two arrays
    arr1 = []
    occurance = {}

    for line in parsed:
        arr1.append(line.split(" ")[0])
        key = line.split(" ")[3]
        occurance[key] = occurance[key] + 1 if key in occurance else 1

    similarity_score = 0

    for line in arr1:
        similarity_score += int(line) * occurance[line] if line in occurance else 0

    return similarity_score


if __name__ == "__main__":
    from aoc.utils import read_input

    data = read_input(1, False)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
