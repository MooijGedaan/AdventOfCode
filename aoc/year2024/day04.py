def parse_as_rows(data: str) -> list[str]:
    return data.strip().splitlines()

def parse_as_columns(data: str) -> list[str]:
    data_as_rows = parse_as_rows(data)
    return ["".join(chars) for chars in zip(*data_as_rows)]

def parse_as_diagonal_tr_bl(data: str) -> list[str]:
    data_as_rows = parse_as_rows(data)

    rows = len(data_as_rows)
    cols = len(data_as_rows[0])
    diagonal_map = {}

    for i in range(rows):
        for j in range(cols):
            key = i + j
            if key not in diagonal_map:
                diagonal_map[key] = []
            diagonal_map[key].append(data_as_rows[i][j])
    
    sorted_keys = sorted(diagonal_map.keys())
    return ["".join(diagonal_map[key]) for key in sorted_keys]

def parse_as_diagonal_tl_br(data: str) -> list[str]:
    data_as_rows = parse_as_rows(data)

    rows = len(data_as_rows)
    cols = len(data_as_rows[0])
    diagonal_map = {}

    for i in range(rows):
        for j in range(cols):
            key = i - j
            if key not in diagonal_map:
                diagonal_map[key] = []
            diagonal_map[key].append(data_as_rows[i][j])
    
    sorted_keys = sorted(diagonal_map.keys())
    return ["".join(diagonal_map[key]) for key in sorted_keys]

def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 1
    """
    parsed_as_rows = parse_as_rows(data)
    parsed_as_cols = parse_as_columns(data)
    parsed_as_diag_1 = parse_as_diagonal_tl_br(data)
    parsed_as_diag_2 = parse_as_diagonal_tr_bl(data)

    all_lines = parsed_as_rows + parsed_as_cols + parsed_as_diag_1 + parsed_as_diag_2
    
    total = 0
    for line in all_lines:
        total += count_xmas(line)
        total += count_xmas(line[::-1])

    return total

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
