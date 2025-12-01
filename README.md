# Advent of Code

Solutions for [Advent of Code](https://adventofcode.com/) puzzles in Python.

## Setup

1. Install Python 3.10 or higher
2. Install the project in development mode:

```bash
pip install -e ".[dev]"
```

## Project Structure

```
.
├── aoc/                 # Solution modules
│   ├── utils.py         # Utility functions for reading input
│   ├── year2024/        # Solutions for 2024
│   │   └── day01.py
│   └── year2025/        # Solutions for 2025
│       └── day01.py
├── inputs/              # Input files (not committed)
│   ├── year2024/
│   │   └── day01.txt
│   └── year2025/
├── tests/               # Test files
│   ├── test_utils.py
│   ├── year2024/
│   └── year2025/
└── pyproject.toml       # Project configuration
```

## Usage

### Adding Input Files

Download your puzzle input from Advent of Code and save it in the `inputs/yearYYYY/` directory:
- `inputs/year2024/day01.txt` for Day 1 of 2024
- `inputs/year2025/day01.txt` for Day 1 of 2025
- etc.

### Running Solutions

To run a specific day's solution, use the module path including the year:

```bash
# Run Day 1 of 2024
python -m aoc.year2024.day01

# Run Day 1 of 2025
python -m aoc.year2025.day01
```

### Running Tests

Run all tests:

```bash
pytest
```

Run tests for a specific year:

```bash
pytest tests/year2024
```

Run tests for a specific day:

```bash
pytest tests/year2025/test_day01.py
```

## Creating a New Day's Solution

1. Copy `aoc/yearYYYY/day01.py` to `aoc/yearYYYY/dayXX.py` (creating the year directory if needed)
2. Create `inputs/yearYYYY/dayXX.txt` with your puzzle input
3. Create `tests/yearYYYY/test_dayXX.py` for your tests
4. Implement your solution!
