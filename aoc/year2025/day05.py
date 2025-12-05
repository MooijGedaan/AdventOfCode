"""
*Approach Part 1
For each ingredient ID (second part of the input), loop over the ingredient ID ranges and 
mathematically check if the range covers the id. If so, increment result.

*Time complexity
Outer loop is O(n), inner part of the loop is O(n), so overall O(n^2)

*Space complexity
O(1) as it is not needed to store any data

*Approach Part 2
First loop over all intervals, create a tuple for each interval and place them inside an array. 
Then sort the array on the first element of the tuple. Then we loop over the resulting list
and merge any range that has an overlap. At last we add up the new, non-overlapping, ranges.

*Time complexity
Building the intervals array takes O(n), sorting takes O(n log n), merging takes another O(n)
and summing every interval takes O(k) where k <= n. So the most dominant term is O(n log n).

*Space complexity
Interval list takes O(n), the new interval list takes O(k) where k <= n. So the space complexity
is O(n).

"""

def parse_input(data: str) -> list[str]:
    """Parse the input data.

    Args:
        data: Raw input string

    Returns:
        Parsed data structure
    """
    return data.strip().split("\n\n")


def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 1
    """
    parsed = parse_input(data)

    result = 0

    for num in parsed[1].split("\n"):
        for num_range in parsed[0].split("\n"):
            start, end = map(int, num_range.split("-"))
            if start <= int(num) <= end:
                result += 1
                break

    return result


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)

    result = 0

    interval_list = []
    new_interval_list = []
    
    for num_range in parsed[0].split("\n"):
        interval = (int(num_range.split("-")[0]), int(num_range.split("-")[1]))
        interval_list.append(interval)

    # Sort on first element of the tuple
    interval_list.sort()
    current_start, current_end = interval_list[0]

    for interval in interval_list[1:]:

        # Get first and second element of tuple
        start, end = interval

        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            new_interval_list.append((current_start, current_end))
            current_start, current_end = start, end
    new_interval_list.append((current_start, current_end))

    for start, end in new_interval_list:
        result += end - start + 1
    
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
