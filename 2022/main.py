import os
import importlib

# Find and run all solution files.

SOLUTION_FILE_NAMES = ['part1.py', 'part2.py', 'solution.py']

for dirpath, dirname, filenames in os.walk('.'):
    for fname in filenames:
        if fname in SOLUTION_FILE_NAMES:
            file = dirpath + '/' + fname
            print(f'--- Running {file} ---')
            modname = file.replace('/', '.').replace('.py', '').lstrip('.')
            mod = importlib.import_module(modname)
            mod.run()
            print()
