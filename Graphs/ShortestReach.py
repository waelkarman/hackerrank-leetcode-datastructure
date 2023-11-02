class Graph:
    
    def __init__(self,n):
        self.size = n
        self.g = {}
        
    def connect(self,u,v):

        if u not in self.g:
            self.g[u]=[]
            self.g[u].append(v)
        else:
            if v not in self.g[u]: #could be avoided
                self.g[u].append(v)
            
        if v not in self.g:
            self.g[v]=[]
            self.g[v].append(u)
        else:
            if u not in self.g[v]: #could be avoided
                self.g[v].append(u)
        
    def find_all_distances(self,k):
        distance = [-1 for _ in range(self.size)]
        self.bfs_distance(k,distance)
        for a in distance:
            print(a,end=' ')
        print("",end="\n")
        return distance
    
    def bfs_distance(self,n,d):
        done = []
        queue=[]
        queue.append(n)
        far = 0
        dist={}
        
        while len(queue) > 0:
            current = queue.pop(0)
            a=d[current]
            if a != -1:
                far = a + 6
            else:
                far = 6
            done.append(current)
            for i in self.g[current]:
                if i not in done:
                    d[i]=far
                    queue.append(i)
        
        del d[n]


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
