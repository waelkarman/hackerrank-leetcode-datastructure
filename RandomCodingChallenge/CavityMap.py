
def cavityMap(grid):
    # Write your code here
    points = []
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if( ((i > 0) and (i <(len(grid[0])-1)))and ( (j > 0) and (j <(len(grid[0])-1)) ) ):
                if grid[i+1][j]<grid[i][j] and grid[i-1][j]<grid[i][j] and grid[i][j+1]<grid[i][j] and grid[i][j-1]<grid[i][j]:
                    points.append((i,j))
    
    for p1,p2 in points:
        grid[p1] = grid[p1][0:p2]+'X'+grid[p1][p2+1:len(grid[0])]
        
    
    return grid
