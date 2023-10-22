

def gridwalkerTab(n,m):
    g = [ [0 for _ in range(m+1) ] for _ in range(n+1) ]
    g[1][1]=1

    for i in range(n+1):
        for j in range(m+1):
            if i+1<=n:
                g[i+1][j]+=g[i][j]
            if j+1<=m:  
                g[i][j+1]+=g[i][j]
    
    #print(g)
    return g[n][m]




print(gridwalkerTab(3,2))
print(gridwalkerTab(2,3))
print(gridwalkerTab(3,3))

