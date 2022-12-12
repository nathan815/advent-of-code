from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass
class CPU:
    x: int = 1


class CpuInstruction:
    name = ""

    def __init__(self) -> None:
        self.complete = False

    def run(self, cpu: CPU, *args):
        pass

    @staticmethod
    def from_name(name: str) -> type["CpuInstruction"]:
        for ins in [AddX, NoOp]:
            if ins.name == name:
                return ins
        raise ValueError()


class NoOp(CpuInstruction):
    name = "noop"
    def run(self, cpu: CPU):
        self.complete = True


class AddX(CpuInstruction):
    name = "addx"
    def __init__(self) -> None:
        super().__init__()
        self.cycles_ran = 0

    def run(self, cpu: CPU, v: str):
        self.cycles_ran += 1
        if self.cycles_ran == 2:
            cpu.x += int(v)
            # print("adding", v, "to x. New x =", cpu.x)
            self.complete = True


def calculate_cycle_signal_strength_sum(cpu_reg_x_values: dict[int, int]):
    signal_sum = 0
    for cycle, x in cpu_reg_x_values.items():
        signal_sum += cycle * x
    return signal_sum


def get_sum_of_signal_6_strengths(cpu_instructions: list[str], max_cycles=220):
    cpu_instructions = cpu_instructions.copy()
    cpu = CPU()
    cpu_reg_x_values = {}

    instruction = None
    cycle = 1

    while len(cpu_instructions) > 0:
        # print("cycle", cycle, end=" ")

        if instruction is None:
            parts = cpu_instructions[0].split(" ")
            iname = parts[0]
            iargs = [] if len(parts) <= 1 else parts[1:]
            instruction = CpuInstruction.from_name(iname)()
            # print("begin", end=" ")

        # track value of X during certain cycles
        if cycle in [20, 60, 100, 140, 180, 220]:
            cpu_reg_x_values[cycle] = cpu.x

        if instruction is not None:
            # print("run", instruction.name, iargs, cpu)
            instruction.run(cpu, *iargs)
            if instruction.complete:
                cpu_instructions.pop(0)
                instruction = None

        cycle += 1

    print(cpu_reg_x_values)
    return calculate_cycle_signal_strength_sum(cpu_reg_x_values)


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        lines = fp.read().splitlines()

    print("Day 9 Part 1 - Sum of first 6 signal strengths during program execution")
    result = get_sum_of_signal_6_strengths(lines)
    print(result)

    return result


if __name__ == "__main__":
    run()
