# SINGLE SOURCE MULTIPLE PATH
# negative weight allowed
import math

g = {
    1:{2:8,3:-2,4:4},
    2:{5:-2},
    3:{2:7,5:3,4:1},
    4:{6:5},
    5:{},
    6:{3:9}
}

def BellmanFord(g,first):
    i=0
    sol = [math.inf for _ in g.keys()]

    while i < len(g.keys())-1: #N-1 loop 
        for key_of_graph in g.keys():
            for key_of_maps in g[key_of_graph].keys():
                if key_of_graph == first :
                    sol[key_of_maps-1] = g[key_of_graph][key_of_maps]

                if sol[key_of_maps-1] > abs(g[key_of_graph][key_of_maps] + sol[key_of_graph-1]):
                    sol[key_of_maps-1] = g[key_of_graph][key_of_maps] + sol[key_of_graph-1]

            print(f"Solution step-by-step : {sol}\n\n")    
        i+=1

BellmanFord(g,1)