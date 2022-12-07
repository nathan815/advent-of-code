import sys

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

WIN = 'win'
LOSS = 'loss'
TIE = 'tie'

move_symbols = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}
outcome_symbols = {
    'X': LOSS,
    'Y': TIE,
    'Z': WIN,
}
move_points = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}
move_outcomes = [
    (ROCK, PAPER, WIN),
    (ROCK, SCISSORS, LOSS),
    (PAPER, ROCK, LOSS),
    (PAPER, SCISSORS, WIN),
    (SCISSORS, ROCK, WIN),
    (SCISSORS, PAPER, LOSS),
]
outcome_points = {
    WIN: 6,
    TIE: 3,
    LOSS: 0,
}


def find_move_for_outcome(opponent_move, desired_outcome):
    if desired_outcome == TIE:
        return opponent_move

    for move1, move2, outcome in move_outcomes:
        if move1 == opponent_move and outcome == desired_outcome:
            return move2

    print('ERROR: Could not find move for outcome. opponent_move=', opponent_move, ' desired_outcome=', desired_outcome)


def find_outcome_for_moves(opponent_move, my_move):
    for move1, move2, outcome in move_outcomes:
        if move1 == opponent_move and move2 == my_move:
            return outcome
    return TIE


def calculate_rock_paper_scissors_total_score(lines):
    score = 0
    for line in lines:
        parts = line.split(' ')
        opponent_move = move_symbols[parts[0].strip()]
        needed_outcome = outcome_symbols[parts[1].strip()]
        my_move = find_move_for_outcome(opponent_move, needed_outcome)
        outcome = find_outcome_for_moves(opponent_move, my_move)
        score += move_points[my_move] + outcome_points[outcome]

    return score


file = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
with open(file, 'r') as fp:
    lines = fp.readlines()
    print('Part 2 - Calculate Total Score Given [OpponentMove, NeededOutcome]')
    result = calculate_rock_paper_scissors_total_score(lines)
    print(result)

    if len(sys.argv) >= 3:
        assert result == int(sys.argv[2])
