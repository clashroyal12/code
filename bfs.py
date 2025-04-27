v, e = map(int, input("Enter number of Vertices & Edges: ").split())
adj = {i: [] for i in range(v)}
visited = {i: False for i in range(v)}

for i in range(e):
    u, vtx = map(int, input("Enter Edge (u v): ").split())
    adj[u].append(vtx)
    adj[vtx].append(u)

source = int(input("Enter Source: "))

def bfs(source):
    queue = [source]
    visited[source] = True

    while queue:
        front = queue.pop(0)  # Slight improvement: use pop(0)

        print(front, end=" ")

        for neighbour in adj[front]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

print("BFS Traversal:", end=" ")
bfs(source)