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

    zero_count = 0
    position = 50

    for line in parsed:
        num = int(line[1:].strip())
        if line[0] == "L":
            position = (position - num) % 100
        elif line[0] == "R":
            position = (position + num) % 100
        
        if position == 0:
            zero_count += 1

    return zero_count


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)

    zero_count = 0
    position = 50

    for line in parsed:
        num = int(line[1:].strip())

        if line[0] == "L":
            zero_count += (position - 1) // 100 - (position - num - 1) // 100
            position = (position - num) % 100

        elif line[0] == "R":
            zero_count += (position + num) // 100
            position = (position + num) % 100
            
    return zero_count


if __name__ == "__main__":
    from aoc.utils import read_input
    import os

    # Get day number
    day_str = os.path.splitext(os.path.basename(__file__))[0]
    day = int(day_str[-2:])

    # Get year number
    year_dir = os.path.basename(os.path.dirname(__file__))
    year = int(year_dir[-4:])

    data = read_input(day, year, False)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
