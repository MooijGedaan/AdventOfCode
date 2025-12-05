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
    for line in parsed:
        for i, _ in enumerate(line):
            if (len(line) < i + 4):
                break

            # Check for a mul
            m = line[i]
            u = line[i+1]
            l = line[i+2]
            opening_par = line[i+3]

            # Encountered a correct setup
            if m == "m" and u == "u" and l == "l" and opening_par == "(":
                fst_num = get_digits(line[i+4:], ",")
                if fst_num == None:
                    continue
                snd_num = get_digits(line[i+5+len(fst_num):], ")")
                if snd_num == None:
                    continue
                total += int(fst_num) * int(snd_num)    
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
    mul_are_enabled = True
    for line in parsed:
        for i, _ in enumerate(line):
            # Check for a do / don't
            if len(line) > i + 1 and line[i] == "d" and line[i+1] == "o":
                # Decide wether it is do or don't
                if len(line) > i + 3 and line[i+2] == "(" and line[i+3] == ")":
                    mul_are_enabled = True
                
                if len(line) > i + 6 and line[i+2] == "n" and line[i+3] == "'" and line[i+4] == "t" and line[i+5] == "(" and line[i+6] == ")":
                    mul_are_enabled = False

            if (len(line) < i + 4):
                break

            # Check for a mul
            m = line[i]
            u = line[i+1]
            l = line[i+2]
            opening_par = line[i+3]

            # Encountered a correct setup
            if m == "m" and u == "u" and l == "l" and opening_par == "(":
                fst_num = get_digits(line[i+4:], ",")
                if fst_num == None:
                    continue
                snd_num = get_digits(line[i+5+len(fst_num):], ")")
                if snd_num == None:
                    continue

                if mul_are_enabled:
                    total += int(fst_num) * int(snd_num)    
    return total

def get_digits(text: str, stopping_char: str) -> str | None:
    number = 0
    result = None
    for char in text:
        if char == stopping_char:
            return result
        if not char.isdigit():
            return None
        if char.isdigit() and number < 3:
            number += 1
            if result is None:
                result = char
            else:
                result += char

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
