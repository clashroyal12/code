def is_safe(board, row, col, n):
    for i in range(col - 1, -1, -1):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def store_configuration(board, configurations):
    temp = []
    for row in board:
        temp.extend(row)
    configurations.append(temp)

def solve(board, col, n, configurations):
    if col == n:
        store_configuration(board, configurations)
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, col + 1, n, configurations)
            board[row][col] = 0

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    configurations = []
    solve(board, 0, n, configurations)
    return configurations

def display_solutions(solutions, n):
    for index, solution in enumerate(solutions):
        print(f"\nSolution {index + 1}:")
        for i in range(n):
            row = ''
            for j in range(n):
                if solution[i * n + j] == 1:
                    row += 'Q '
                else:
                    row += '. '
            print(row)
        print('-' * (2 * n))

# Example usage
n = 4
solutions = n_queens(n)
print(f"Total Solutions: {len(solutions)}")
display_solutions(solutions, n)