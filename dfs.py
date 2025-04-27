v= int(input("Enter the number of vertices: "))
e= int(input("Enter the number of edges: "))

adj= {i: [] for i in range(1, v+1)}
for i in range(e):
    u, v= map(int, input("Enter edge: ").split())
    adj[u].append(v)
    adj[v].append(u)

visited= {i: False for i in range(1, v+1)}

def dfs(vertex):
    visited[vertex]= True

    print(vertex, end= " ")

    for neighbour in adj[vertex]:
        if not visited[neighbour]:
            dfs(neighbour)

source= int(input("Enter the source vertex: "))
print("DFS Traversal: ", end= " ")
dfs(source)