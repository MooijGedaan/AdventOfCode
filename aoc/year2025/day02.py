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
    parsed = parse_input(data)[0].split(",")

    total = 0
    seen_double = []
    seen_not_double = []

    for ranges in parsed:
        range_arr = ranges.split("-")
        for i in range(int(range_arr[0]), int(range_arr[1]) + 1):
            if i in seen_double:
                total += i
                continue
            elif i in seen_not_double:
                continue

            if double_number(str(i)):
                seen_double.append(i)
            else:
                seen_not_double.append(i)
    return total

def double_number(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    
    half = len(s) // 2
    return s[:half] == s[half:]


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)[0].split(",")

    total = 0
    seen_double = set()
    seen_not_double = set()

    for ranges in parsed:
        range_arr = ranges.split("-")
        for i in range(int(range_arr[0]), int(range_arr[1]) + 1):
            if i in seen_double:
                total += i
                continue
            elif i in seen_not_double:
                continue

            if check_substring(str(i)):
                seen_double.add(i)
                total += i
            else:
                seen_not_double.add(i)
            
    return total

def check_substring(s: str) -> bool:
    length = len(s)
    for size in range(1, length // 2 + 1):
        if length % size != 0:
            continue
        pattern = s[:size]
        multiplier = length // size

        if pattern * multiplier == s:
            return True
    return False

if __name__ == "__main__":
    from aoc.utils import read_input

    data = read_input(2, sample=False, year=2025)
    # print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
