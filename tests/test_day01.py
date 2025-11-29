"""Tests for Day 01 solution."""

from aoc.day01 import parse_input, part1, part2


def test_parse_input() -> None:
    """Test input parsing."""
    data = "line1\nline2\nline3"
    result = parse_input(data)
    assert result == ["line1", "line2", "line3"]


def test_part1_placeholder() -> None:
    """Placeholder test for part 1."""
    # TODO: Add real test with example data
    assert part1("") == 0


def test_part2_placeholder() -> None:
    """Placeholder test for part 2."""
    # TODO: Add real test with example data
    assert part2("") == 0
