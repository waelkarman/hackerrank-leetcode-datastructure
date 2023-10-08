#   SINGLE SOURCE MULTIPLE PATH
# DFS and BFS for undirected graphs

g={
    1:[2,3],
    2:[1,3],
    3:[1,2,4,7],
    4:[3,5,6],
    5:[4],
    6:[4],
    7:[3]
}

# iterative
def dfs(g,first):
    queue = [first]
    done = []
    while len(queue)>0:
        position=queue.pop()
        done.append(position)
        print(position)
        for p in g[position]:
            if p not in queue and p not in done :
                queue.append(p)

# recursive
def dfs_recursive(g,first,done):
    print(f"{first}")
    done.append(first)
    for p in g[first]:
        if p not in done:
            dfs_recursive(g,p,done)

# iterative
def bfs(g,first):
    stack = [first]
    done = []

    while len(stack)>0:
        position=stack.pop(0)
        done.append(position)
        print(position)
        for p in g[position]:
            if(p not in stack and p not in done):
                stack.append(p)

# recursive
def bfs_recursive(g,first,queue,done):
    print(f"{first}")
    done.append(first)
    for p in g[first]:
        if p not in queue and p not in done:
            queue.append(p)
    if len(queue)>0:
        bfs_recursive(g,queue.pop(0),queue,done)



l=list(g.keys())
print("DFS:")
dfs(g,l[0])
print("BFS:")
bfs(g,l[0])
#RECURSIVE
print("DFS_recursive:")
queue=[]
dfs_recursive(g,l[0],queue)
print("BFS_recursive:")
queue=[]
done=[]
bfs_recursive(g,l[0],queue,done)
