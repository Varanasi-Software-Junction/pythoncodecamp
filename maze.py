def SolveMaze(maze, start, end, path, visited):

    
    
    path.append(start)
    visited.add(start)
    
    
    if start == end:
        return path
    
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for direction in directions:
        row = start[0] + direction[0]
        col = start[1] + direction[1]
        neighbor = (row, col)
        
        if (row>=0 and row< len(maze)) and (col>=0 and  col < len(maze[0])) and (maze[row][col] != 1) and (neighbor not in visited):
            result = SolveMaze(maze, neighbor, end, path.copy(), visited.copy())
            if result: 
                return result
    
    return None 


maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
start = (1, 1)
end = (3, 3)
path=[]
visited=set()


solution = SolveMaze(maze, start, end,path,visited)
if solution:
    print("Path found:", solution)
else:
    print("No path found")
