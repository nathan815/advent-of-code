def part1_find_most_elf_calories(lines):
    max_elf_calories = 0
    current_elf_calories = 0
    for line in lines:
        if line.strip() == '':
            current_elf_calories = 0
        else:
            try:
                current_elf_calories += int(line)
            except ValueError:
                pass
        if current_elf_calories > max_elf_calories:
            max_elf_calories = current_elf_calories
    return max_elf_calories
                

def part2_find_top_3_elf_calories_sum(lines):
    current_elf_calories = 0
    all_elf_calories = []

    for line in lines:
        if line.strip() == '':
            all_elf_calories.append(current_elf_calories)
            current_elf_calories = 0
            continue

        try:
            current_elf_calories += int(line)
        except ValueError:
            pass

    all_elf_calories.append(current_elf_calories)

    all_elf_calories.sort(reverse=True)

    total = 0
    for cals in all_elf_calories[0:3]:
        print('adding', cals)
        total += cals
    return total


with open('input.txt', 'r') as fp:
    lines = fp.readlines()
    print('Part 1 - Calories Carried by Top Elf')
    print(part1_find_most_elf_calories(lines))

    print('Part 2 - Sum of Calories Carried by Top 3 Elfs')
    print(part2_find_top_3_elf_calories_sum(lines))
