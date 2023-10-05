
def dfs(g,init=1):
    queue = []
    done = []
    queue.append(init)
    current = None
    while len(queue) > 0:
        if current is not None:
            done.append(current)
        current = queue.pop() 
        for c in g[current]:
            if c not in queue and c not in done:
                queue.append(c)
    return done
    
# Naive
def transitiveClosure(g):
    for i in g.keys():
        print(f"i:{i} -> {dfs(g,i)}")

print("Transitive Closure: ")

g={
    1:[3],
    2:[3],
    3:[4,7],
    4:[6],
    5:[4],
    6:[5],
    7:[]
}

transitiveClosure(g)
