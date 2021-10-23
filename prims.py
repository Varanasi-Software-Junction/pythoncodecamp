class Edge:
    def __init__(this, fromloc, toloc, dist):
        this.fromloc = fromloc
        this.toloc = toloc
        this.dist = dist

    def __str__(self):
        return "From {0} to {1} dis {2}".format(self.fromloc, self.toloc, self.dist)


def printEdges(edges):
    for edge in edges:
        print(edge)


mat = [[0, 2, 0, 6, 0],
       [2, 0, 3, 8, 5],
       [0, 3, 0, 0, 7],
       [6, 8, 0, 0, 9],
       [0, 5, 7, 9, 0]]
edges = []
n = len(mat)
for y in range(n):
    for x in range(n):
        fromloc = y
        toloc = x
        dist = mat[y][x]
        if y == x:
            dist = -1
        edges = edges + [Edge(fromloc, toloc, dist)]
printEdges(edges)
