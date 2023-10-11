
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    #p=1
    #d=100
    #m=1
    #s=9777
    cost=0
    num=0
    while p > m:
        cost+=p
        num+=1
        if cost > s:
            break
        p=p-d
    print("till now: ",num)
    while cost < s:
        cost += m
        num+=1    
        
    return num-1
        

