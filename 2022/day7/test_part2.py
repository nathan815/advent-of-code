from pathlib import Path
from day7.part2 import run_day7_part2

def test_run_with_sample():
    assert run_day7_part2(file=Path(__file__).parent / 'sample_input.txt') == 24933642
