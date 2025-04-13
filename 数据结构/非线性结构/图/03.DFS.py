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

def dfs_2(n,path,u,limit):
    u.color = "gray"
    path.append(u)
    if n < limit:
        neighbors = sorted(list(u.get_neighbors()))
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].color == "white":
                done = dfs_2(n + 1,path,neighbors[i],limit)
                i = i + 1

        if not done:
            path.pop()
            u.color = "white"
    else:
        done = True
    return done


















































