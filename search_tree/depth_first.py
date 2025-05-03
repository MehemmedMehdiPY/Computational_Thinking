"""
Fun fact: Code perfectly worked when I ran it at the first trial with only knowledge about algorithm.

--------- ALGORITHM DESCRIPTION ---------
In general, a depth-first-search algorithm begins by choosing one child of the start node. 
It then chooses one child of that node and so on, going deeper and deeper until it either reaches the goal node or 
a node with no children. The search then backtracks, returning to the most recent node with children that 
it has not yet visited. 


Branch should return the path so that each path can be compared.
If no destination found on the path, then return None
If destination found on path, then compare the size with the destination found on another path
to make sure that the shortest one is chosen.
"""

def DFS(node_start, node_end, graph, path = [], shortest_path = None):
    path = path + [node_start]
    
    if node_start == node_end:
        return path

    for node_child in graph[node_start]:
        if node_child not in path:
            path_from_branch = DFS(node_child, node_end, graph, path, shortest_path)
            if shortest_path is None or len(shortest_path) > len(path_from_branch):
                shortest_path = path_from_branch
    return shortest_path

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

print(DFS(7, 0, graph))