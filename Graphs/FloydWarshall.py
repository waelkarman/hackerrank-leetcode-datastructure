
# Floyd-Warshall  ~ Dynamic
def floydWarshall(g):
    matrix = [[-1 for _ in range(len(g.keys()))] for _ in range(len(g.keys()))]
    # fill an adjacency matrix
    for n in g.keys():
        for e in g[n].keys():
            matrix[n-1][e-1] = g[n][e]
   
    #compute matrix for i in (1-len(g.keys()))

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j!=k and i!= k and i!=j:
                    checkBetter(matrix,i,j,k)        

    print(f"{matrix}")            

def checkBetter(matrix,i,j,k):
    if matrix[i][k] != -1 and matrix[k][j] != -1 :
        if matrix[i][j] != -1 and matrix[i][k] + matrix[k][j] < matrix[i][j]:
            matrix[i][j] = matrix[i][k] + matrix[k][j]
        if matrix[i][j] == -1 :
            matrix[i][j] = matrix[i][k] + matrix[k][j]



print("Floyd Washall: ")
g={
    1:{3:10,2:4},
    2:{3:2},
    3:{4:8,7:2},
    4:{6:1,7:1},
    5:{4:3},
    6:{5:2},
    7:{}
}

floydWarshall(g)