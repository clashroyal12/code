# Hardcoded graph details
v = 4
e = 4

adj = {i: [] for i in range(v)}
heuristic = {
    0: 5,
    1: 3,
    2: 4,
    3: 0
}

# Defining edges
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 3, 3),
    (2, 1, 2)
]

# Build adjacency list
for u, vtx, w in edges:
    adj[u].append((vtx, w))
    adj[vtx].append((u, w))  # Assuming undirected graph

# Define source and goal
source = 0
goal = 3

def a_star(source, goal):
    open_list = [[heuristic[source], 0, source]]  # [f(n), g(n), node]
    closed_list = set()
    parent = {source: None}

    while open_list:
        # Find node with minimum f(n)
        min_idx = 0
        for i in range(len(open_list)):
            if open_list[i][0] < open_list[min_idx][0]:
                min_idx = i
        
        f, g, node = open_list.pop(min_idx)

        if node in closed_list:
            continue

        print(node, end=" ")

        if node == goal:
            print("\nGoal reached!")
            return

        closed_list.add(node)

        for neighbour, weight in adj[node]:
            if neighbour not in closed_list:
                g_new = g + weight
                f_new = g_new + heuristic[neighbour]
                # Check if neighbour already in open_list with better cost
                found = False
                for item in open_list:
                    if item[2] == neighbour and item[0] <= f_new:
                        found = True
                        break
                if not found:
                    open_list.append([f_new, g_new, neighbour])
                    if neighbour not in parent:
                        parent[neighbour] = node

    print("\nGoal not reachable!")

a_star(source, goal)