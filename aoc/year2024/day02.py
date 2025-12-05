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
    
    total_safe = 0

    for line in parsed:
        input_as_array = line.split(" ")
        safe = True

        is_increasing = False
        is_decreasing = False

        for i, char in enumerate(input_as_array):
            # Check if there is one more character available
            if safe and i + 1 < len(input_as_array):
                char = int(char)
                next_char = int(input_as_array[i + 1])
                
                if char == next_char:
                    # Not increasing or decreasing
                    safe = False
                elif abs(char - next_char) > 3:
                    # Difference more than 3
                    safe = False
                elif char > next_char and (not is_increasing):
                    # Decreasing sequence
                    is_decreasing = True
                elif char > next_char and is_increasing:
                    # Decreasing sequence, while it should be increasing
                    safe = False
                elif char < next_char and (not is_decreasing):
                    # Increasing sequence
                    is_increasing = True
                elif char < next_char and is_decreasing:
                    # Increasing sequence, while it should be decreasing
                    safe = False
        
        if safe:
            total_safe += 1

    return total_safe


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)
    
    total_safe = 0

    for line in parsed:
        input_as_array = line.split(" ")

        for i, _ in enumerate(input_as_array):
            if check_safety(input_as_array[:i] + input_as_array[i+1:], False, False):
                total_safe += 1
                break
    return total_safe

def check_safety(line: list[str], is_increasing: bool, is_decreasing: bool) -> bool:
    if len(line) <= 1:
        return True
    
    fst = int(line[0])
    snd = int(line[1])

    if fst == snd:
        return False
    elif abs(fst - snd) > 3:
        return False
    elif fst > snd and (not is_increasing):
        return check_safety(line[1:], False, True)
    elif fst > snd and is_decreasing:
        return False
    elif fst < snd and (not is_decreasing):
        return check_safety(line[1:], True, False)
    elif fst < snd and is_increasing:
        return False
    
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
