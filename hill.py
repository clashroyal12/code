# Objective function
def f(x):
    return -x * x + 10 * x

# Simple manual random number generator (just for starting point)
def simple_random(start, end):
    seed = 7  # fixed seed for simple randomness
    seed = (seed * 1103515245 + 12345) % (2**31)
    rand = seed / (2**31)
    return start + (end - start) * rand

# Hill Climbing algorithm
def hill_climb(start, step_size=0.1, max_iters=1000):
    current = start
    current_val = f(current)

    for i in range(max_iters):
        # Try moving left or right
        left = current - step_size
        right = current + step_size

        left_val = f(left)
        right_val = f(right)

        # Move to better neighbor
        if left_val > current_val:
            current, current_val = left, left_val
        elif right_val > current_val:
            current, current_val = right, right_val
        else:
            break  # Local maximum reached

    return current, current_val

# Example usage
start = 2  # You can manually choose a starting point like 2
best_x, best_val = hill_climb(start)

print("Started at x =", round(start, 2))
print("Local Maximum at x =", round(best_x, 2), ", f(x) =", round(best_val, 2))