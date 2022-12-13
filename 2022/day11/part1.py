from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from pprint import pprint
import sys
from typing import Tuple


@dataclass(kw_only=True)
class Monkey:
    num: int
    inspected_item_count: int = 0
    holding_items: list[int]
    operation: str
    test: str
    test_true_throw_to: int
    test_false_throw_to: int

    def inspect_item(self):
        item = self.holding_items[0]
        # print("Monkey", self.num, "inspecting item 0", item)
        self.inspected_item_count += 1
        self.holding_items[0] = calc_new_worry_level(self.operation, item)
        # print("Updated item 0 worry level to", self.holding_items[0], end=" ")

    def test_item(self) -> bool:
        test_result = run_worry_level_test(self.test, self.holding_items[0])
        # print(f"Item 0 test [{self.test}] =", test_result, end=" ")
        return test_result

    def throw_item(self, other_monkey: "Monkey"):
        item = self.holding_items.pop(0)
        # print(f"Throwing item {item} to {other_monkey.num}")
        other_monkey.catch_item(item)

    def catch_item(self, item: int):
        self.holding_items.append(item)


def run_worry_level_test(test: str, worry_level: int) -> bool:
    parts = test.split(" ")
    if test.startswith("divisible by"):
        return worry_level % int(parts[2]) == 0
    return False


def calc_new_worry_level(operation: str, old: int) -> int:
    def convert_operand(operand: str | int) -> int:
        if operand == "old":
            return old
        return int(operand)

    # ex: new = old + 6
    parts = operation.split("=")[1].strip().split(" ")
    operator = parts[1]
    operand1 = convert_operand(parts[0])
    operand2 = convert_operand(parts[2])
    if operator == "+":
        new_level = operand1 + operand2
    elif operator == "*":
        new_level = operand1 * operand2
    else:
        raise ValueError(f"unknown operator {operator} in operation {operation}")

    return int(new_level / 3)


def play_monkey_in_the_middle(
    monkeys: list[Monkey], rounds=20
) -> Tuple[list[Monkey], int]:
    for round in range(0, rounds):
        for monkey in monkeys:
            # print("Round", round, monkey.holding_items, monkey)

            while len(monkey.holding_items) > 0:
                monkey.inspect_item()
                test_result = monkey.test_item()
                throw_to = (
                    monkey.test_true_throw_to
                    if test_result
                    else monkey.test_false_throw_to
                )
                monkey.throw_item(monkeys[throw_to])

    monkeys_sorted = sorted(monkeys, key=lambda m: m.inspected_item_count, reverse=True)
    # pprint(monkeys_sorted)
    monkey_business_level = reduce(
        lambda product, m: product * m.inspected_item_count,
        monkeys_sorted[0:2],
        1,
    )
    return monkeys, monkey_business_level


def parse_monkeys(input: str) -> list[Monkey]:
    line_groups = input.split("\n\n")
    monkeys = []
    for group in line_groups:
        lines = [line.strip() for line in group.splitlines()]
        if len(lines) > 0:
            monkeys.append(
                Monkey(
                    num=int(lines[0].replace("Monkey ", "", 1).rstrip(":")),
                    holding_items=[
                        int(item)
                        for item in lines[1]
                        .replace("Starting items: ", "", 1)
                        .split(",")
                    ],
                    operation=lines[2].replace("Operation: ", "", 1),
                    test=lines[3].replace("Test: ", "", 1),
                    test_true_throw_to=int(
                        lines[4].replace("If true: throw to monkey ", "", 1)
                    ),
                    test_false_throw_to=int(
                        lines[5].replace("If false: throw to monkey ", "", 1)
                    ),
                )
            )
    return monkeys


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        input = fp.read()

    print("Day 11 Part 1 - Level of monkey business of 2 most active monkeys")
    monkeys = parse_monkeys(input)
    _, result = play_monkey_in_the_middle(monkeys)
    print(result)

    return result


if __name__ == "__main__":
    run()
