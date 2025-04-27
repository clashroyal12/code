# Node structure
class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost  # g(n): cost from start to current node
        self.heuristic = heuristic  # h(n): estimated cost to goal
        self.f = cost + heuristic  # f(n) = g(n) + h(n)

    def path(self):
        node, p = self, []
        while node:
            p.append(node.state)
            node = node.parent
        return p[::-1]  # reversed path

# Example graph
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 5)],
    'D': [('G', 1)],
    'G': []  # Goal
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 4,
    'D': 1,
    'G': 0
}

# Memory bounded search
def memory_bounded_search(start, goal, memory_limit):
    frontier = [Node(start, None, 0, heuristic[start])]

    while frontier:
        # Sort frontier based on f-value (smallest first)
        frontier.sort(key=lambda node: node.f)
        current = frontier.pop(0)

        # Goal test
        if current.state == goal:
            return current.path()

        # Expand children
        for neighbor, cost in graph.get(current.state, []):
            child = Node(neighbor, current, current.cost + cost, heuristic[neighbor])
            frontier.append(child)

        # Enforce memory limit
        if len(frontier) > memory_limit:
            # Remove node with highest f-value (worst option)
            frontier.sort(key=lambda node: node.f, reverse=True)
            removed_node = frontier.pop(0)
            print(f"Removing node {removed_node.state} to maintain memory bound.")

    return None

# Example usage
path = memory_bounded_search('S', 'G', memory_limit=3)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")