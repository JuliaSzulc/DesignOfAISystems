from Tree import *
import numpy as np


GRID_DIM = 3
AI_SYMBOL = 'x'
USER_SYMBOL = 'o'


def update_grid(grid, coordinates, symbol):
    grid[coordinates[0], coordinates[1]] = symbol
    return grid


if __name__ == '__main__':
    grid = np.full((GRID_DIM, GRID_DIM), '')
    tree = Tree(AI_SYMBOL, grid, 2)

    winner = tree.check_winner(grid)
    user_turn = False
    round_count = 0

    while not winner and round_count < GRID_DIM**2:
        if user_turn:
            print("Your move")
            user_input = input(
                "Write coordinates (0-{}) separated with space\n".format(
                    GRID_DIM - 1)).split()
            user_coordinates = (int(user_input[0]), int(user_input[1]))
            grid = update_grid(grid, user_coordinates, USER_SYMBOL)
        else:
            print("AI move")
            ai_coordinates = tree.run(grid, USER_SYMBOL)
            grid = update_grid(grid, ai_coordinates, AI_SYMBOL)

        print(grid)

        winner = tree.check_winner(grid)
        if winner:
            if winner == USER_SYMBOL:
                print("You won!")
                break
            print("AI won!")
            break

        user_turn = not user_turn
        round_count += 1

    print("Draw!")