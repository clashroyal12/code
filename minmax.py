# Define infinity manually
infinity = 999999

# Example game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

# Functions same as before
def is_terminal(state):
    return isinstance(tree[state], int)

def utility(state):
    return tree[state]

def actions(state):
    return tree[state]

def result(state, action):
    return action

# Modified Minimax to also return the path
def minmax(state, depth, maximizing_player):
    if is_terminal(state) or depth == 0:
        return utility(state), [state]
    
    if maximizing_player:
        max_eval = -infinity
        best_path = []
        for action in actions(state):
            eval, path = minmax(result(state, action), depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_path = [state] + path
        return max_eval, best_path
    else:
        min_eval = infinity
        best_path = []
        for action in actions(state):
            eval, path = minmax(result(state, action), depth - 1, True)
            if eval < min_eval:
                min_eval = eval
                best_path = [state] + path
        return min_eval, best_path

# Example usage
start_state = 'A'
depth = 3

best_value, best_path = minmax(start_state, depth, True)

print("The optimal value is:", best_value)
print("The path taken is:", " -> ".join(best_path))