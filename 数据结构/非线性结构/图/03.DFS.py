graph = {
    "A": ["B", "C"],
    "B": ["A", "C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E","F"],
    "E": ["C","D"],
    "F": ["D"],
}

def dfs_1(graph,s):
    stack = [s]
    seen = set()
    seen.add(s)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                seen.add(w)
                stack.append(w)

        print(vertex)

#test
dfs_1(graph,"A")






















































