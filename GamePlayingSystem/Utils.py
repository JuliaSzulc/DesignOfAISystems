def update_grid(grid, coordinates, symbol):
    grid[coordinates[0], coordinates[1]] = symbol
    return grid


def check_winner(grid):
    dimension = grid.shape[0]
    
    for i in range(dimension):
        char = grid[0][i]
        if all(grid[j][i] == char for j in range(1, dimension)):
            return char

    for j in range(dimension):
        char = grid[j][0]
        if all(grid[j][i] == char for i in range(1, dimension)):
            return char

    char = grid[0][0]
    if all(grid[i][i] == char for i in range(1, dimension)):
        return char

    char = grid[0][-1]
    if all(grid[i][-1 - i] == char for i in range(1, dimension)):
        return char
    return None
