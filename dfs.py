def dfs(graph, a, b, path=[], visited=[], current=None):
    if (current is None):
        current = a
    if ((current in visited) is False):
        visited.append(current)
    for x in graph:
        if (x[0] == current):
            if ((x[1] in visited) is False) :
                visited.append(x[1])
                path.append([current, x[1]])
                if (x[1] != b):
                    dfs(graph, a, b, path, visited, x[1])
        if (x[1] == current):
            if ((x[0] in visited) is False):
                visited.append(x[0])
                path.append([current, x[0]])
                if (x[0] != b):
                    dfs(graph, a, b, path, visited, x[0])
    return len(path)


test = [[1,2], [2, 3], [3, 4], [3,5]]
path =  dfs(test, 1, 3)
print(path)