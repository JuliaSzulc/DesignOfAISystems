from MCTreeSearch import *
from User import *
from Utils import check_winner, update_grid

import numpy as np
from random import getrandbits
from copy import deepcopy
from collections import Counter


def train(empty_grid, ai_player, epochs=10):
    for epoch in range(epochs):
        print("Epoch {}/{}".format(epoch, epochs), end='\r')

        dummy = MCTreeSearch(OPPONENT_SYMBOL, empty_grid, SIMULATION_STEPS,
                             name='dummy', strategy='reward')

        grid = np.copy(empty_grid)
        play(grid, ai_player, dummy, prints=False)
        ai_player.reset()


def test(empty_grid, trained_ai, trials=20):
    results = Counter()

    for trial in range(trials):
        print("Trial {}/{}".format(trial, trials), end='\r')
        ai_player = deepcopy(trained_ai)
        dummy = MCTreeSearch(OPPONENT_SYMBOL, empty_grid, SIMULATION_STEPS,
                             name='dummy', strategy='reward')

        grid = np.copy(empty_grid)
        result = play(grid, ai_player, dummy, prints=False)
        results.update(result)
        ai_player.reset()

    print("Win: {}, Loss: {}, Draw: {}".format(
        results[AI_SYMBOL], results[OPPONENT_SYMBOL], results['-']))


def play(grid, ai_player, opponent, prints=True):
    if prints:
        print(grid)

    players = {True: ai_player, False: opponent}
    turn = bool(getrandbits(1))

    round_count = 0
    winner_symbol = None

    while not winner_symbol and round_count < (grid.shape[0])**2:
        player = players[turn]
        if prints:
            print("Turn: {} ({})".format(player.name, player.symbol))
        coordinates = player.make_move(grid)
        grid = update_grid(grid, coordinates, player.symbol)

        if prints:
            print(grid)

        winner_symbol = check_winner(grid)
        if winner_symbol:
            winner = ai_player if ai_player.symbol == winner_symbol else opponent
            if prints:
                print("{} ({}) won!".format(winner.name, winner_symbol))
            break

        turn = not turn
        round_count += 1

    if not winner_symbol:
        winner_symbol = '-'
        if prints:
            print("Draw!")

    return winner_symbol


if __name__ == '__main__':
    GRID_DIM = 3
    AI_SYMBOL = 'x'
    OPPONENT_SYMBOL = 'o'
    SIMULATION_STEPS = 2

    empty_grid = np.full((GRID_DIM, GRID_DIM), '')

    ai_uct = MCTreeSearch(AI_SYMBOL, empty_grid, SIMULATION_STEPS,
                          name='AI_uct', strategy='uct')
    ai_reward = MCTreeSearch(OPPONENT_SYMBOL, empty_grid, SIMULATION_STEPS,
                             name='AI_reward', strategy='reward')
    user = User(OPPONENT_SYMBOL)

    # play(empty_grid, ai_uct, ai_reward)
    train(np.copy(empty_grid), ai_uct, 50)
    test(np.copy(empty_grid), ai_uct, 20)

    while True:
        play(np.copy(empty_grid), deepcopy(ai_uct), user)
