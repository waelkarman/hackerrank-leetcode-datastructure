def maxRegion(grid):
    # Write your code here
    g={}
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                g[f"{i}-{j}"]=[]
                
                if (i+1) < len(grid) and grid[i+1][j] == 1 :
                    g[f"{i}-{j}"].append(f"{i+1}-{j}")
                if (i-1) >= 0  and grid[i-1][j] == 1 :
                    g[f"{i}-{j}"].append(f"{i-1}-{j}")
                    
                if (j+1) < len(grid[0]) and grid[i][j+1] == 1 :
                    g[f"{i}-{j}"].append(f"{i}-{j+1}")
                if (j-1) >= 0 and grid[i][j-1] == 1 :
                    g[f"{i}-{j}"].append(f"{i}-{j-1}")

                if (j+1) < len(grid[0]) and (i+1) < len(grid) and grid[i+1][j+1] == 1 :
                    g[f"{i}-{j}"].append(f"{i+1}-{j+1}")
                if (j-1) >=0 and (i-1) >=0 and grid[i-1][j-1] == 1 :
                    g[f"{i}-{j}"].append(f"{i-1}-{j-1}")
                if (j-1) >=0 and (i+1) < len(grid) and grid[i+1][j-1] == 1 :
                    g[f"{i}-{j}"].append(f"{i+1}-{j-1}")
                if (j+1) < len(grid[0]) and (i-1) >=0 and grid[i-1][j+1] == 1 :
                    g[f"{i}-{j}"].append(f"{i-1}-{j+1}")

    
    print(g)
    n=countdfs(g)
    return n

def countdfs(g):
    if g is None:
        return 0
    
    done = []
    maxnum=0
    while len(g.keys()) > len(done):
        k=0
        for a in g:
            if a not in done:
                k=a
                break
        #k=list(g)[0]
        num=0
        queue = []
        queue.append(k)
        while len(queue) > 0:
            current=queue.pop(0)
            num+=1
            done.append(current)
            for n in g[current]:
                if n not in done and n not in queue:
                    queue.append(n)
                
        if num > maxnum:
            maxnum=num    
    return maxnum