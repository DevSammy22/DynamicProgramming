#mine
def shortest_path_DAG(edges, n):

    f = [float("inf")] * (n + 1) # this keeps the distance
    f[1] = 0
    pi = [None] * (n + 1) # this keeps the shortest path

    adj = [[] for _ in range(n + 1)]
    for (v, u, w) in edges: # v = j; u = i
        adj[u].append((v, w))

    for i in range(2, (n + 1)):
        for (v, w) in adj[i]:
            if f[i] > f[v] + w:
                f[i] = f[v] + w
                pi[i] = v

    return f, pi

def print_path(t, pi):
    if t == 1:
        print(1, end="")
        return
    print_path(pi[t], pi)
    print(f"==> {t}", end=" ")

# Example usage
# Example usage
n = 5  # Number of nodes
edges = [
    (1, 2, 3),   # edge from node 1 to 2 with weight 3
    (1, 3, 6),   # edge from node 1 to 3 with weight 6
    (2, 3, 4),   # edge from node 2 to 3 with weight 4
    (2, 4, 4),   # edge from node 2 to 4 with weight 4
    (3, 5, 2),   # edge from node 3 to 5 with weight 2
    (4, 5, 1)    # edge from node 4 to 5 with weight 1
]

distance, path = shortest_path_DAG(edges, n)
print("The distance from node 1: ")
for i in range(1, (n + 1)):
    print(f"Node {i} :  {distance[i]}")

print("\nThe path from node 1: ")
for t in range(1, (n + 1)):
    print(f"Path from Node 1 to Node {t}: ", end = " ")
    print_path(t, path)
    print()