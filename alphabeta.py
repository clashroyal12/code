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

# Minimax with alpha-beta pruning and path tracking
def alphabeta(state, depth, alpha, beta, maximizing_player):
    if is_terminal(state) or depth == 0:
        return utility(state), [state]
    
    if maximizing_player:
        max_eval = -infinity
        best_path = []
        for action in actions(state):
            eval, path = alphabeta(result(state, action), depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_path = [state] + path
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval, best_path
    else:
        min_eval = infinity
        best_path = []
        for action in actions(state):
            eval, path = alphabeta(result(state, action), depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_path = [state] + path
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval, best_path

# Example usage
start_state = 'A'
depth = 3

best_value, best_path = alphabeta(start_state, depth, -infinity, infinity, True)

print("The optimal value is:", best_value)
print("The path taken is:", " -> ".join(best_path))