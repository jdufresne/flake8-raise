import subprocess
import sys
from pathlib import Path

import pytest

DATADIR = Path(__file__).parent / "data"


def generate_testdata():
    for path in sorted(DATADIR.glob("*.py")):
        yield path


def generate_test_id(path):
    return path.stem


@pytest.mark.parametrize("path", generate_testdata(), ids=generate_test_id)
def test_checks(path):
    result = subprocess.run(
        [sys.executable, "-m", "flake8", "--isolated", str(path.relative_to(DATADIR))],
        cwd=str(DATADIR),
        stdout=subprocess.PIPE,
    )
    try:
        expected = path.with_suffix(".txt").read_bytes()
    except FileNotFoundError:
        expected = b""
    assert result.stdout == expected
