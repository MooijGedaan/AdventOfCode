def parse_input(data: str) -> list[str]:
    """Parse the input data.

    Args:
        data: Raw input string

    Returns:
        Parsed data structure
    """
    rows = []
    for line in data.strip().splitlines():
        line = line.strip()
        if line.startswith("*") or line.startswith("+"):
            break
        nums = [int(x) for x in line.split()]
        rows.append(nums)

    cols = [list(rows) for rows in zip(*rows)]

    return cols

def parse_operators(data: str) -> list[str]:
    for line in data.strip().splitlines():
        if line.startswith("*") or line.startswith("+"):
            return [c for c in line.strip() if c not in " "]

def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 1
    """
    parsed = parse_input(data)
    operators = parse_operators(data)

    result = 0

    for id, line in enumerate(parsed):
        total = 0
        operator = operators[id]
        for num in line:
            if operator == "*":
                if total == 0:
                    total = 1
                total *= num
            elif operator == "+":
                total += num
        result += total
    return result

def special_parse(data: str) -> list[str]:
    data_lines = [line.rstrip('\n') for line in data.strip().splitlines()[:-1]]
    
    # Determine the maximum width to pad shorter lines if necessary
    max_len = max(len(line) for line in data_lines)
    padded_lines = [line.ljust(max_len) for line in data_lines]

    # Transpose the grid: rows become columns
    # zip(*padded_lines) creates tuples of characters for each column index
    cols = [''.join(chars) for chars in zip(*padded_lines)]

    parsed_columns = []

    for col_str in cols:
        # If the column is entirely whitespace, it's a separator, skip it
        if not col_str.strip():
            parsed_columns.append("|")  # Use None to indicate a separator
            continue

        cleaned_num = col_str.replace(' ', '')
        if cleaned_num:
            parsed_columns.append(int(cleaned_num))
    print(parsed_columns)
    return parsed_columns

def get_numbers_from_parsed(parsed: list[str], id: int) -> list[int]:
    numbers = []
    seperator_count = 0
    for item in parsed:
        if item == "|":
            seperator_count += 1
            continue
        if seperator_count == id:
            numbers.append(item)
        elif seperator_count > id:
            break
    return numbers


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = special_parse(data)

    result = 0

    for id, operator in enumerate(parse_operators(data)):
        total = 0

        for num in get_numbers_from_parsed(parsed, id):
            if operator == "*":
                if total == 0:
                    total = 1
                total *= num
            elif operator == "+":
                total += num
        result += total
    return result

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
