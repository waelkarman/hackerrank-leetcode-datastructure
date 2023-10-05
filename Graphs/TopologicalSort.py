
g = {
    1:[],
    2:[],
    3:[1],
    4:[1,2,3],
    5:[2,4,6],
    6:[3],
    7:[5,6],
    8:[3],
    9:[5,7,8]
}


#can be implemented faster by using a priority queue based on a heap

def TopologicalSort(g):
    sol = []
    
    f = find_next_free_node(g)
    while f is not None:
        f = find_next_free_node(g)
        if f is not None:
            delete_node_from_graph(g,f)
            sol.append(f)        

    print(sol)

def delete_node_from_graph(g,f):
    del g[f]
    for i in g:
        while f in g[i]:
            g[i].remove(f)
            
def find_next_free_node(g):
    for i in g:
        if len(g[i])==0:
            return i
    return None



TopologicalSort(g)