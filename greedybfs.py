# Priority Queue without libraries
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(reverse=True)  # lowest priority (heuristic) first

    def get(self):
        return self.elements.pop()[1]

# Define the graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values for each node (Estimated cost to goal 'G')
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

# Greedy Best First Search Algorithm
def greedy_bfs(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put(start, heuristic[start])
    path = []

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

# Example usage
start_node = 'A'
goal_node = 'G'

path = greedy_bfs(start_node, goal_node)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not reachable.")