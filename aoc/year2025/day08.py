import numpy as np

"""
*Approach Part 1
First calculate all distances between points and sort them in ascending order based on distance.
Then loop over these distances and connect the closest two points that are not already connected.
Keep track of the number of connections made, stop when 1000 is reached.
Use union-find to keep track of connected components.

*Explanation Union-find
Every point is represented in the parent list, initially pointing to itself (every point is their
own parent). When two points are connected, the root of one point is made to point to the root of 
the other point. The smaller one points to the larger one to keep the tree flat.
"""

def parse_input(data: str) -> np.ndarray:
    """Parse the input data.

    Args:
        data: Raw input string

    Returns:
        Parsed data structure
    """
    values = []
    row = []
    for line in data.splitlines():
        row = [int(digit) for digit in line.split(",")]
        values.append(row)

    return np.array(values, dtype=int)

def find(x: int, parent: list[int]) -> int:
    """
    Finds the representative (root) of the set containing element x.

    This function traverses the parent array upwards until it finds the root of the tree
    (an element that is its own parent).
    """
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a: int, b: int, parent: list[int], size: list[int]) -> bool:
    """
    Merges the sets containing elements a and b.

    If the elements are already in the same set, returns False.
    Otherwise, merges the smaller set into the larger set and returns True.

    Returns:
        bool: True if the sets were merged (they were disjoint), 
        False if they were already in the same set.
    """
    ra, rb = find(a, parent), find(b, parent)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

def distance_between_all_points(n: int, parsed: np.ndarray) -> list[tuple[float, int, int]]:
    """
    Calculate the Euclidean distance between all pairs of points. Avoids duplicate distances.

    Args:
        n: Number of points
        parsed: Array of points

    Returns:
        List of tuples containing (distance, index1, index2)
    """
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.linalg.norm(parsed[i] - parsed[j])
            edges.append((dist, i, j))
    edges.sort(key=lambda x: x[0])
    return edges

def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 1
    """
    parsed = parse_input(data)

    n = len(parsed)
    target_connections = 1000

    # Union-Find list initialization
    parent = list(range(n))
    size = [1] * n

    edges = distance_between_all_points(n, parsed)

    # Make connections until target is reached
    connections_made = 0
    for dist, i, j in edges:
        if connections_made >= target_connections:
            break
        union(i, j, parent, size)
        connections_made += 1
    
    # Count the sizes of each connected component
    comp_sizes = {}
    for v in range(n):
        r = find(v, parent)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1

    largest = sorted(comp_sizes.values(), reverse=True)

    while len(largest) < 3:
        largest.append(1)

    return largest[0] * largest[1] * largest[2]


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: Raw input string

    Returns:
        Solution to part 2
    """
    parsed = parse_input(data)

    n = len(parsed)

    parent = list(range(n))
    size = [1] * n

    edges = distance_between_all_points(n, parsed)

    last_range = 0

    for dist, i, j in edges:
        if union(i, j, parent, size):
            last_range = parsed[i][0] * parsed[j][0]
            pass

    return last_range

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
