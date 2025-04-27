# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]   # 0 represents the blank tile
]

# Directions for moving the blank tile
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Helper function to find the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Helper function to generate a new state after moving
def move(state, direction):
    x, y = find_blank(state)
    dx, dy = directions[direction]
    new_x, new_y = x + dx, y + dy

    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_state = [row[:] for row in state]  # Deep copy
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
    return None

# DFS search
def dfs(initial_state, depth_limit=30):
    stack = [(initial_state, [])]  # (state, path)

    visited = []

    while stack:
        state, path = stack.pop()

        if state == goal_state:
            return path

        if state in visited:
            continue
        visited.append(state)

        if len(path) >= depth_limit:
            continue  # depth limit reached, stop expanding

        for dir in directions.keys():
            new_state = move(state, dir)
            if new_state and new_state not in visited:
                stack.append((new_state, path + [dir]))

    return None  # no solution found

# Helper function to print the state nicely
def print_state(state):
    for row in state:
        print(' '.join(str(cell) for cell in row))
    print()

# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Initial State:")
print_state(initial_state)

solution = dfs(initial_state)

if solution:
    print("Solution found!")
    print("Moves:", solution)

    # Let's simulate the moves:
    current_state = initial_state
    for move_dir in solution:
        current_state = move(current_state, move_dir)
        print(f"Move {move_dir}:")
        print_state(current_state)

else:
    print("No solution found.")