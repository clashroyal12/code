# Priority Queue without libraries
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(reverse=True)  # smallest heuristic first

    def get(self):
        return self.elements.pop()[1]

# Example graph (Adjacency List)
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': ['G'],
    'G': []   # Goal
}

# Heuristic values (Estimated cost to goal)
heuristic = {
    'S': 5,
    'A': 3,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'G': 0
}

# Greedy Best First Search Algorithm
def greedy_best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put(start, heuristic[start])
    path = []  # To track the final path

    while not pq.empty():
        current = pq.get()
        path.append(current)

        if current == goal:
            return path

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put(neighbor, heuristic[neighbor])

    return None

# Example usage:
start_node = 'S'
goal_node = 'G'
result_path = greedy_best_first_search(start_node, goal_node)

if result_path:
    print("Path:", " -> ".join(result_path))
else:
    print("Goal not reachable.")