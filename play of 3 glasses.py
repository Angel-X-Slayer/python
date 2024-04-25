def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def dfs(node, graph, values, visited):
    visited[node] = True
    subtree_sum = values[node - 1]
    for neighbor in graph[node]:
        if not visited[neighbor]:
            subtree_sum += dfs(neighbor, graph, values, visited)
    return subtree_sum


def primeSumSubtrees(n, edges, values):
    graph = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = [False] * (n + 1)
    count_good_subtrees = 0
    for node in range(1, n + 1):
        visited = [False] * (n + 1)
        subtree_sum = dfs(node, graph, values, visited)
        if is_prime(subtree_sum % (10**5 + 3)):
            count_good_subtrees += 1
    return count_good_subtrees


# Example usage:
N = 3
k = 1
edges = [[1, 3], [1, 2]]
values = [0, 1, 2]
print(primeSumSubtrees(N, edges, values))
