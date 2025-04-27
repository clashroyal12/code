import math

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initial empty board
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

def print_board(b):
    for row in b:
        print('|'.join(row))
    print()

def is_moves_left(b):
    return any(EMPTY in row for row in b)

def evaluate(b):
    # Row check
    for row in b:
        if row.count(AI) == 3:
            return +10
        elif row.count(HUMAN) == 3:
            return -10
    # Column check
    for col in range(3):
        if all(b[row][col] == AI for row in range(3)):
            return +10
        elif all(b[row][col] == HUMAN for row in range(3)):
            return -10
    # Diagonal check
    if all(b[i][i] == AI for i in range(3)):
        return +10
    elif all(b[i][i] == HUMAN for i in range(3)):
        return -10
    if all(b[i][2 - i] == AI for i in range(3)):
        return +10
    elif all(b[i][2 - i] == HUMAN for i in range(3)):
        return -10
    return 0

def minimax(b, depth, is_max):
    score = evaluate(b)

    if score == 10 or score == -10:
        return score
    if not is_moves_left(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    best = max(best, minimax(b, depth + 1, not is_max))
                    b[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = HUMAN
                    best = min(best, minimax(b, depth + 1, not is_max))
                    b[i][j] = EMPTY
        return best

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                move_val = minimax(b, 0, False)
                b[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

alternate= 1
score= 0
while is_moves_left(board):
    print_board(board)
    
    if alternate == 1:
        i, j= map(int, input("Enter Move(i, j): ").split())
        board[i][j]= HUMAN
    else:
        i, j= find_best_move(board)
        board[i][j]= AI
    alternate= 1 - alternate

    score = evaluate(board)
    if score == 10 or score == -10:
        break

print_board(board)

if score == 10:
    print("AI Wins!")
elif score == -10:
    print("HUMAN Wins!")
else:
    print("Draw!")