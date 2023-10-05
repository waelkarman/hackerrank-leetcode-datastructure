
# using a priority queue based on heap improve the selection of the next node to relax

def Dijkstra(g,next):
    sol = {}
    relaxed = []
    relaxable = []
    current_distance = 0

    while next != -1:
        relaxed.append(next)
        relax(g,next,current_distance,relaxable,relaxed,sol)
        val = select_the_next(relaxable,current_distance)
        next=val[0]
        current_distance=val[1]
        print("sol:",sol)
        print("relaxed:",relaxed)
        print("relaxable:",relaxable)
        print("current_distance:",current_distance)
        print("Next:",next)
        print("________________________________")

def relax(g,next,current_distance,relaxable,relaxed,sol):
    for i in g[next]:    
        
        if i[0] not in relaxed:
            relaxable.append(i)

        if i[0] not in sol:
            sol[i[0]] = current_distance+i[1]
        else:    
            if current_distance+i[1] < sol[i[0]]:
                sol[i[0]] = current_distance+i[1]
    
def select_the_next(relaxable,current_distance):
    next = -1
    if len(relaxable)==0:
        return next,current_distance
    
    i=0
    to_delete=0
    min=relaxable[0][1]
    next=relaxable[0][0]
    while i < len(relaxable):
        if min > relaxable[i][1]:
            min=relaxable[i][1]
            next=relaxable[i][0]
            to_delete=i
        i+=1
    print(f"to_delete:{relaxable[to_delete][0]}")    
    current_distance+=min
    del relaxable[to_delete]
    return next,current_distance

g={
    1:[(2,2),(3,4)],
    2:[(3,1),(4,7)],
    3:[(5,3)],
    4:[(6,1)],
    5:[(4,2),(6,5)],
    6:[]
}

Dijkstra(g,1)