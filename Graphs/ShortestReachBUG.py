
# TO BE FIXED !
# BFS used since edges have all the same lenght and compute distance is possible with a lower computational complexity withrespect to the other algorithms 

class Graph:
    
    def __init__(self,n):
        self.size = n
        self.g = {}
        
    def connect(self,u,v):
        if u not in self.g:
            self.g[u]=[]
            self.g[u].append(v)
        else:
            self.g[u].append(v)
            
        if v not in self.g:
            self.g[v]=[]
            self.g[v].append(u)
        else:
            self.g[v].append(u)
        
    def find_all_distances(self,k):
        distance = [-1 for _ in range(self.size)]
        self.bfs_distance(k,distance)
        for a in distance:
            print(a,end=' ')
        print("",end="\n")
        #return distance
    
    def bfs_distance(self,n,d):
        #print(f"initial d:{d}")
        layers={}
        done = []
        queue=[]
        queue.append(n)
        layers[n]=1
        current_old=n
        km=0
        while len(queue) > 0:
            current = queue.pop(0)
            #print(f"current:{current}")
            layers[current_old]-=1
            #print(f"assigning to {current} = km:{km}")
            d[current]=km
            if layers[current_old]==0:
                km+=6
                print(f"level up")
            
            done.append(current)
            for i in self.g[current]:
                if i not in done:
                    layers[current]+=1
                    layers[i]=1
                    queue.append(i)
            current_old=current
        d.remove(0)
        #print(f"d:{d}")
        
        
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        #print(f"(x-1,y-1):({x-1},{y-1}) ")
        graph.connect(x-1,y-1) 
    s = int(input())
    #print(f"g:{graph.g}")
    graph.find_all_distances(s-1)


