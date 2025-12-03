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

    total = 0

    for bank in parsed:
        first_digit = max(bank[:-1])
        first_idx = bank.find(first_digit)
        second_digit = max(bank[first_idx + 1:])
        print(f"{int(first_digit + second_digit)}")
        total += int(first_digit + second_digit)

    return total

def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)
    total = 0

    for bank in parsed:
        result = ""
        prev_idx = -1
        for num in range(12):
            needed_after = 11 - num
            start = prev_idx + 1
            end = len(bank) - needed_after
            window = bank[start:end]

            maximum_number = max(window)
            max_idx = bank.find(maximum_number, start, end)
            result += maximum_number
            prev_idx = max_idx
        print(f"result: {result}")

        total += int(result)

    return total

if __name__ == "__main__":
    from aoc.utils import read_input

    data = read_input(3, sample=False, year=2025)
    # print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
