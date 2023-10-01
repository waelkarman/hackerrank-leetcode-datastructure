class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        g = {}
        for p in prerequisites:
            if g.get(p[0]) is None:
                g[p[0]] = []    
                g[p[0]].append(p[1])
                if g.get(p[1]) is None:
                    g[p[1]] = []
            else:
                g[p[0]].append(p[1])
                if g.get(p[1]) is None:
                    g[p[1]] = []

        count = 0
        for y in range(numCourses-1):
            to_del=[]
            for k in g.keys(): 
                if len(g[k]) == 0:
                    count +=1
                    to_del.append(k)
                    for q in g.keys():
                        if k in g[q]: 
                            g[q].remove(k)
            for d in to_del:
                del g[d]

        if len(g)==0 or count >= numCourses-1:
            return True

        return False