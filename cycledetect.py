def printMatrix(mat):
    print()
    n = len(mat)
    print('\t', end="")
    for i in range(n):
        ch = chr(ord('A')+i)
        print(ch, end="\t")
    print()
    for i in range(n):
        print(end="\t")
        for j in range(n):
            value = mat[i][j]

            if value >= infinity:
                value = '∞'
            elif value <= 0:
                value = ""
            print(value, end="\t")
        print()


def findAllReachableVertices(mat, position):
    n = len(mat)
    visited = [0 for x in range(n)]
    visited[position] = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i == position:
                continue
            if (mat[position][i] < infinity) and (mat[i][j] < infinity):
                visited[j] = 1

    # print(visited)
    return visited


infinity = 10000000
graph = [[-1, 1, 0, 1], [1, 0, 1, 1],
         [0, 1, 0, 1], [1, 1, 1, 0]]

printMatrix(graph)
result = findAllReachableVertices(graph, 0)
print(result)
