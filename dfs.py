def dfs(graph, path,  visited, current):
    if ((current in visited) is False):
        visited.append(current)
    for x in graph:
        if (x[0] == current):
            if ((x[1] in visited) is False):
                visited.append(x[1])
                path.append([current, x[1]])
                dfs(graph, path, visited, x[1])
        if (x[1] == current):
            if ((x[0] in visited) is False):
                visited.append(x[0])
                path.append([current, x[0]])
                dfs(graph, path, visited, x[0])
    return path


test = [[1,2], [2, 3], [3, 4], [3,5]]
print('path', dfs(test, [], [], 1))