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
    current_beams = set()
    total_count = 0

    for line in parsed:
        if len(current_beams) == 0:
            current_beams.add(line.find("S"))
            continue

        next_beams = set()

        for beam in current_beams:
            if line[beam] == "^":
                total_count += 1
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)
            if line[beam] == ".":
                next_beams.add(beam)

        current_beams = next_beams
    return total_count

def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)
    current_beams = {}

    for line in parsed:
        if len(current_beams) == 0:
            current_beams[line.find("S")] = 1
            continue
        
        next_beams = {}

        for index, count in current_beams.items():
            if line[index] == "^":
                if index - 1 in next_beams:
                    next_beams[index - 1] += count
                else:
                    next_beams[index - 1] = count
                
                if index + 1 in next_beams:
                    next_beams[index + 1] += count 
                else:
                    next_beams[index + 1] = count


            if line[index] == ".":
                if index in next_beams:
                    next_beams[index] += count
                else:
                    next_beams[index] = count
        
        current_beams = next_beams
        
    return sum(current_beams.values())

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
