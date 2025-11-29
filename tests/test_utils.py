"""Tests for utility functions."""

import pytest
from pathlib import Path
from aoc.utils import read_input, read_lines, read_ints


@pytest.fixture
def sample_input(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Create a sample input file for testing."""
    inputs_dir = tmp_path / "inputs"
    inputs_dir.mkdir()
    input_file = inputs_dir / "day01.txt"
    input_file.write_text("1\n2\n3\n4\n5\n")

    # Patch the utils module to use our tmp path
    monkeypatch.setattr(
        "aoc.utils.read_input",
        lambda day, year=2024: (inputs_dir / f"day{day:02d}.txt").read_text().strip()
    )
    return inputs_dir


def test_read_input_returns_string(sample_input: Path) -> None:
    """Test that read_input returns file contents as string."""
    from aoc.utils import read_input
    result = read_input(1)
    assert isinstance(result, str)
    assert result == "1\n2\n3\n4\n5"


def test_read_lines_returns_list(sample_input: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that read_lines returns a list of strings."""
    from aoc import utils
    monkeypatch.setattr(
        utils, "read_input",
        lambda day, year=2024: (sample_input / f"day{day:02d}.txt").read_text().strip()
    )

    result = utils.read_lines(1)
    assert result == ["1", "2", "3", "4", "5"]


def test_read_ints_returns_integers(sample_input: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that read_ints returns a list of integers."""
    from aoc import utils
    monkeypatch.setattr(
        utils, "read_input",
        lambda day, year=2024: (sample_input / f"day{day:02d}.txt").read_text().strip()
    )

    result = utils.read_ints(1)
    assert result == [1, 2, 3, 4, 5]
