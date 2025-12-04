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
    return 0

def count_xmas(line: str) -> int:
    total = 0
    for id, _ in enumerate(line):
        if len(line) < id + 4:
            continue

        X_1 = line[id]
        M = line[id+1]
        A = line[id+2]
        S = line[id+3]

        if X_1 == "X" and M == "M" and A == "A" and S == "S":
            total += 1
    return total

def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed_as_rows = parse_as_rows(data)

    total = 0

    for id, line in enumerate(parsed_as_rows):
        if id == 0 or id == len(parsed_as_rows) - 1:
            continue

        for id_char, char in enumerate(line):
            if id_char == 0 or id_char == len(line) - 1:
                continue

            if char == "A":
                tl = parsed_as_rows[id - 1][id_char - 1]
                tr = parsed_as_rows[id - 1][id_char + 1]
                bl = parsed_as_rows[id + 1][id_char - 1]
                br = parsed_as_rows[id + 1][id_char + 1]

                if ((tl == "M" and br == "S") or (tl == "S" and br == "M")) and ((tr == "M" and bl == "S") or (tr == "S" and bl == "M")):
                    total += 1

    return total


if __name__ == "__main__":
    from aoc.utils import read_input

    data = read_input(4, sample=False)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
