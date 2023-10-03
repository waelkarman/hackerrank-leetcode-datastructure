
g={
    1:[2,3,4],
    2:[1,3,5],
    3:[1,4,6],
    4:[1,3,6],
    5:[2,3],
    6:[3,4]
}


def dfs(g):
    l=list(g.keys())
    queue = [l[0]]
    done = []
    while len(queue)>0:
        position=queue.pop()
        done.append(position)
        print(position)
        for p in g[position]:
            if p not in queue and p not in done :
                queue.append(p)


def bfs(g):
    l=list(g.keys())
    stack = [l[0]]
    done = []

    while len(stack)>0:
        position=stack.pop(0)
        done.append(position)
        print(position)
        for p in g[position]:
            if(p not in stack and p not in done):
                stack.append(p)

print("DFS:")
dfs(g)
print("BFS:")
bfs(g)
