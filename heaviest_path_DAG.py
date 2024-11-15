#mine
def heaviest_path(edges, n):
    f = [-float("inf")] * (n + 1)
    f[1] = 0

    adj = [[] for _ in range(n + 1)]
    for (u, v, w) in edges:
        adj[u].append((v, w))

    for i in range(1, (n + 1)):
        for (v, w) in adj[i]:
            f[v] = max(f[v], f[i] + w)

    return f[1:], max(f[1:])


# Example usage
n = 5  # Number of nodes
edges = [
    (1, 2, 3),  # Edge from 1 to 2 with weight 3
    (1, 3, 2),  # Edge from 1 to 3 with weight 2
    (2, 4, 4),  # Edge from 2 to 4 with weight 4
    (3, 4, 1),  # Edge from 3 to 4 with weight 1
    (4, 5, 5)   # Edge from 4 to 5 with weight 5
]

heaviest_path_list, max_heaviest_path = heaviest_path(edges, n)
print("The list of heaviest path: ", heaviest_path_list)
print("Maximum heaviest path: ", max_heaviest_path)
