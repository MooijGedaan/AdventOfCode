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

    result = 0

    for x, line in enumerate(parsed):
        for y, char in enumerate(line):
            if char == ".":
                continue            
            if check_adjacent(parsed, x, y, len(line), len(parsed)) <= 3:
                result += 1
    return result

def check_adjacent(arr: list[int], x: int, y: int, num_cols: int, num_rows: int) -> int:
    paper_roll_count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < num_rows and 0 <= ny < num_cols:
                if arr[nx][ny] == "@": paper_roll_count += 1
    return paper_roll_count


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)
    result = 0
    removed_rol = True
    rolls_to_remove = []
    
    while removed_rol is True: 
        removed_rol = False
        for x, line in enumerate(parsed):
            for y, char in enumerate(line):
                if char == ".":
                    continue
                if check_adjacent(parsed, x, y, len(line), len(parsed)) <= 3:
                    result += 1
                    rolls_to_remove.append((x,y))
                    removed_rol = True

                
        for x, y in rolls_to_remove:
            parsed[x] = parsed[x][:y] + "." + parsed[x][y+1:]
        rolls_to_remove = []

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
