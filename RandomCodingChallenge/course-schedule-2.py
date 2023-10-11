class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if len(prerequisites) == 0:
            l = []
            for a in range(numCourses):
                l.append(a)
            return l

        g = {}
        for req in prerequisites:
            if req[0] not in g.keys():
                g[req[0]] = []
                g[req[0]].append(req[1])
                if req[1] not in g.keys():
                    g[req[1]] = []
            else:
                g[req[0]].append(req[1])
                if req[1] not in g.keys():
                    g[req[1]] = []

        course_list=[]
        count=0
        while len(g.keys()) > 0 and count < numCourses:
            count+=1
            to_del=[]
            for key in g.keys(): 
                if len(g[key]) == 0:
                    to_del.append(key)
                    for j in g.keys():
                        if key in g[j] :
                            g[j].remove(key)

            for d in to_del:
                course_list.append(d)
                del g[d]

        if len(g) == 0:
            for i in range(numCourses):
                if i not in course_list:
                    course_list.insert(0,i) 
        else:
            course_list=[]

        return course_list