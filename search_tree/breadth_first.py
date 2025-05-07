"""
I just wrote the code for 15-20 minutes and did not refer to any source code 
to recall the algorithm. It seems I fully grasped these algorithms. 
"""

from depth_first import DFS

def BFS(node_start, node_end, graph):
    path = [[node_start]]
    nodes_visited = []

    while path != []:
        path_current = path.pop(0)
        node_start = path_current[-1]
        
        if node_start == node_end:
            return path_current
        
        for node_child in graph[node_start]:
            if node_child not in nodes_visited:
                path_current_new = path_current + [node_child]
                path.append(path_current_new)
                nodes_visited.append(node_child)
    return None


graph = {
    0: [1, 2, 6], 
    1: [3, 6], 
    2: [1, 0], 
    3: [2, 5], 
    4: [5], 
    5: [0, 4], 
    6: [5],
    7: [], 
}

start = 6
end = 0
print("DFS results:", DFS(start, end, graph))
print("BFS results:", BFS(start, end, graph))