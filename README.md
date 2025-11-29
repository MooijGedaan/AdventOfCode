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
│   ├── __init__.py
│   ├── utils.py         # Utility functions for reading input
│   └── day01.py         # Template/solution for Day 1
├── inputs/              # Input files (not committed)
│   └── day01.txt
├── tests/               # Test files
│   ├── test_utils.py
│   └── test_day01.py
└── pyproject.toml       # Project configuration
```

## Usage

### Adding Input Files

Download your puzzle input from Advent of Code and save it in the `inputs/` directory:
- `inputs/day01.txt` for Day 1
- `inputs/day02.txt` for Day 2
- etc.

### Running Solutions

```bash
python -m aoc.day01
```

### Running Tests

```bash
pytest
```

## Creating a New Day's Solution

1. Copy `aoc/day01.py` to `aoc/dayXX.py`
2. Create `inputs/dayXX.txt` with your puzzle input
3. Create `tests/test_dayXX.py` for your tests
4. Implement your solution!