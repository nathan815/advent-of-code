from pathlib import Path
import sys

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

WIN = 'win'
LOSS = 'loss'
TIE = 'tie'

move_symbols = {
    'A': ROCK,
    'X': ROCK,
    'B': PAPER,
    'Y': PAPER,
    'C': SCISSORS,
    'Z': SCISSORS,
}
move_points = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}
move_outcome = {
    (ROCK, PAPER): WIN,
    (ROCK, SCISSORS): LOSS,
    (PAPER, ROCK): LOSS,
    (PAPER, SCISSORS): WIN,
    (SCISSORS, ROCK): WIN,
    (SCISSORS, PAPER): LOSS,
}
outcome_points = {
    WIN: 6,
    TIE: 3,
    LOSS: 0,
}


def calculate_rock_paper_scissors_round(opponent_move, my_move):
    outcome = move_outcome.get((opponent_move, my_move), TIE)
    return move_points[my_move] + outcome_points[outcome]


def calculate_rock_paper_scissors_total_score(lines):
    score = 0
    for line in lines:
        parts = line.split(' ')
        try:
            opponent = move_symbols[parts[0].strip()]
            mine = move_symbols[parts[1].strip()]
            score += calculate_rock_paper_scissors_round(opponent, mine)
        except KeyError as e:
            print('INVALID LINE:', line, e)
            pass

    return score


def run(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.readlines()
        print('Day 2 Part 1 - Calculate Total Score Given [OpponentMove, MyMove]')
        print(calculate_rock_paper_scissors_total_score(lines))

if __name__ == "__main__":
    run()
