

# PRIM ALGORITHM DIRTY SOLUTION

g = {
    1:{2:2,5:7,3:8},
    2:{1:2,3:5,4:7},
    3:{1:8,2:5,4:9,5:8},
    4:{2:7,3:9,6:4},
    5:{1:7,3:8,6:3},
    6:{4:4,5:3}
}


def prim(g, first):
    
    sol = []
    pickable = []

    current = first
    updatePickable(g,pickable,current,sol)
    
    while len(sol) < len(g.keys())-1:
        current = selectNext(g,pickable,current,sol)
        updatePickable(g,pickable,current,sol)

def updatePickable(g,p,c,s):
    for d in g[c]:
        exist=False
        for element in p:
            if d == element[0] and c == element[2]:
                exist=True
            elif d == element[2] and g[c][d] <= element[1]:
                exist=True
                element[1]=g[c][d]
                element[0]=c
            elif d == element[2] and g[c][d] > element[1]:
                exist=True

        for element in s:
            if d == element[0] and c == element[2]:
                exist=True
            if d == element[2] and c == element[0]:
                exist=True

        if not exist:
            inside=False
            for element in s:
                if element[0] == d:
                    inside=True
            if not inside :
                p.append([c,g[c][d],d])

def selectNext(g,p,c,s):
    new_current = p[0][2]
    min = p[0][1]
    old_source = p[0][0]
    for element in p:
        if min > element[1]:
            old_source = element[0]
            min = element[1]
            new_current = element[2]
    
    print(f"P:{p} ---------> remove and add to solution [{old_source},{min},{new_current}]")
    p.remove([old_source,min,new_current])
    
    s.append([old_source,min,new_current])
    print(f"picked: {new_current}")
    return new_current

prim(g,1)