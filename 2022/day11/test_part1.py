import copy
from pathlib import Path
from day11.part1 import (
    parse_monkeys,
    calc_new_worry_level,
    run_worry_level_test,
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
        test="divisible by 23",
        test_true_throw_to=2,
        test_false_throw_to=3,
    ),
    Monkey(
        num=1,
        holding_items=[54, 65, 75, 74],
        operation="new = old + 6",
        test="divisible by 19",
        test_true_throw_to=2,
        test_false_throw_to=0,
    ),
    Monkey(
        num=2,
        holding_items=[79, 60, 97],
        operation="new = old * old",
        test="divisible by 13",
        test_true_throw_to=1,
        test_false_throw_to=3,
    ),
    Monkey(
        num=3,
        holding_items=[74],
        operation="new = old + 3",
        test="divisible by 17",
        test_true_throw_to=0,
        test_false_throw_to=1,
    ),
]


def test_parse_monkeys():
    output = parse_monkeys(sample_input)
    assert output == sample_monkeys


def test_run():
    assert run(Path(__file__).parent / 'sample_input.txt') == 10605


def test_play_monkey_in_the_middle():
    monkeys, monkey_business_level = play_monkey_in_the_middle(copy.deepcopy(sample_monkeys))
    assert monkeys[0].inspected_item_count == 101
    assert monkeys[1].inspected_item_count == 95
    assert monkeys[2].inspected_item_count == 7
    assert monkeys[3].inspected_item_count == 105
    assert monkey_business_level == 10605


def test_run_worry_level_test():
    assert run_worry_level_test("divisible by 10", 10) == True
    assert run_worry_level_test("divisible by 10", 20) == True
    assert run_worry_level_test("divisible by 20", 10) == False
    assert run_worry_level_test("divisible by 5", 10) == True
    assert run_worry_level_test("divisible by 6", 10) == False
    assert run_worry_level_test("divisible by 2", 1) == False
    assert run_worry_level_test("divisible by 5", 0) == True


def test_calc_new_worry_level():
    assert calc_new_worry_level("new = old * 10", 5) == 16
    assert calc_new_worry_level("new = old * old", 5) == 8
    assert calc_new_worry_level("new = 3 * old", 2) == 2
    assert calc_new_worry_level("new = 3 * 3", 2) == 3
    assert calc_new_worry_level("new = 1 + old", 29) == 10
    assert calc_new_worry_level("new = 1 * old", 12) == 4
