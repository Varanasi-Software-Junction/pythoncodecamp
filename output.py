def isNegativeWeightCycle(self, n, edges):
    dist = [float("inf")] * n
    dist[0] = 0

    for i in range(n - 1):
        updated = False
    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            updated = True
    if not updated:
        return 0

    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            return 1

    return 0