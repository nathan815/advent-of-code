from pathlib import Path
from day10.part1 import run, calculate_cycle_signal_strength_sum

def test_run():
    assert run(Path(__file__).parent / 'sample_input.txt') == 13140

def test_calculate_cycle_signal_strength_sum():
    calculate_cycle_signal_strength_sum({ 1: 2, 2: 5, 3: 10 }) == 42
    calculate_cycle_signal_strength_sum({ 20: 2, 60: 3, 100: 2 }) == 420
