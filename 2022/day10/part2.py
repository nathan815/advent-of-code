from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass
class CPU:
    x: int = 1


class CRT:
    """Cathode Ray Tube Display"""

    def __init__(self, width=40, height=6) -> None:
        self.width = width
        self.height = height
        self.draw_pos = 0, 0
        self.pixels = []
        for i in range(0, height):
            self.pixels.append([])
            for _ in range(0, width):
                self.pixels[i].append(None)

    def draw(self, sprite_midpoint: int):
        """
        Draws single pixel on CRT at current position if sprite is positioned on this pixel
        and moves to next draw position. The sprite is 3 pixels wide.
        """
        x, y = self.draw_pos

        is_sprite_visible = sprite_midpoint-1 <= x <= sprite_midpoint+1
        self.pixels[y][x] = is_sprite_visible

        # print(x, y, is_sprite_visible)

        # go to next draw pos
        x = (x + 1) % self.width
        if x == 0:
            y = (y + 1) % self.width
        self.draw_pos = x, y
    
    def render(self):
        output = []
        for i, row in enumerate(self.pixels):
            row_pixels = ''
            for pixel in row:
                row_pixels += '#' if pixel else '.'
            output.append(row_pixels)
            # print(output)
        return output


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
            self.complete = True


def execute_instructions(cpu_instructions: list[str], max_cycles=220) -> CRT:
    cpu_instructions = cpu_instructions.copy()
    cpu = CPU()
    crt = CRT()

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

        crt.draw(cpu.x)

        if instruction is not None:
            # print("run", instruction.name, iargs, cpu)
            instruction.run(cpu, *iargs)
            if instruction.complete:
                cpu_instructions.pop(0)
                instruction = None

        cycle += 1

    return crt


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        lines = fp.read().splitlines()

    print("Day 9 Part 2 - Rendered CRT image")
    crt = execute_instructions(lines)
    result = '\n'.join(crt.render())
    print(result)

    return result


if __name__ == "__main__":
    run()
