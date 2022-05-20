def staircase(n):
    # Write your code here
    n=n+2
    for i in range(1,n):
        #print(f"STAMPO i:{i}")
        if(i==1):
            continue
        
        for a in range(1,n-i):
            print(' ',end='')
        for b in range(1,i):
            print('#',end='')
        print('')    
