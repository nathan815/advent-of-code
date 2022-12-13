import copy
from pathlib import Path
from day11.part2 import (
    parse_monkeys,
    play_monkey_in_the_middle,
    run,
    Monkey,
)

sample_input = """
Monkey 0:
    Starting items: 79, 98
    Operation: new = old * 19
    Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3

Monkey 1:
    Starting items: 54, 65, 75, 74
    Operation: new = old + 6
    Test: divisible by 19
        If true: throw to monkey 2
        If false: throw to monkey 0

Monkey 2:
    Starting items: 79, 60, 97
    Operation: new = old * old
    Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3

Monkey 3:
    Starting items: 74
    Operation: new = old + 3
    Test: divisible by 17
        If true: throw to monkey 0
        If false: throw to monkey 1
""".strip()

sample_monkeys = [
    Monkey(
        num=0,
        holding_items=[79, 98],
        operation="new = old * 19",
        test_divisor=23,
        test_true_throw_to=2,
        test_false_throw_to=3,
    ),
    Monkey(
        num=1,
        holding_items=[54, 65, 75, 74],
        operation="new = old + 6",
        test_divisor=19,
        test_true_throw_to=2,
        test_false_throw_to=0,
    ),
    Monkey(
        num=2,
        holding_items=[79, 60, 97],
        operation="new = old * old",
        test_divisor=13,
        test_true_throw_to=1,
        test_false_throw_to=3,
    ),
    Monkey(
        num=3,
        holding_items=[74],
        operation="new = old + 3",
        test_divisor=17,
        test_true_throw_to=0,
        test_false_throw_to=1,
    ),
]


def test_parse_monkeys():
    output = parse_monkeys(sample_input)
    assert output == sample_monkeys


def test_run():
    assert run(Path(__file__).parent / "sample_input.txt") == 2713310158


def test_play_monkey_in_the_middle():
    monkeys, monkey_business_level = play_monkey_in_the_middle(
        copy.deepcopy(sample_monkeys)
    )
    assert monkeys[0].inspected_item_count == 52166
    assert monkeys[1].inspected_item_count == 47830
    assert monkeys[2].inspected_item_count == 1938
    assert monkeys[3].inspected_item_count == 52013
    assert monkey_business_level == 2713310158
