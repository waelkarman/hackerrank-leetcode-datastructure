
g = {
    1:{2:2,5:7,3:8},
    2:{1:2,3:5,4:7},
    3:{1:8,2:5,4:9,5:8},
    4:{2:7,3:9,6:4},
    5:{1:7,3:8,6:3},
    6:{4:4,5:3}
}

# by using a priority queue the algorithm could be improved 
# having a graph defined as edge list could speed up the algorithm 
def kruskal(g,first):
    orderedEdges = []
    mts = {}
    
    for graph_nodes_keys in g.keys():
        for single_node_vertex_keys in g[graph_nodes_keys].keys():
            if len(orderedEdges) == 0 :
                orderedEdges.append([g[graph_nodes_keys][single_node_vertex_keys],graph_nodes_keys,single_node_vertex_keys])
            i=0
            while i<len(orderedEdges) and g[graph_nodes_keys][single_node_vertex_keys] >= orderedEdges[i][0]:
                if orderedEdges[i][1] == graph_nodes_keys and orderedEdges[i][2] == single_node_vertex_keys:
                    i=-1
                    break
                if orderedEdges[i][2] == graph_nodes_keys and orderedEdges[i][1] == single_node_vertex_keys:
                    i=-1
                    break
                i+=1
            if i!=-1:
                orderedEdges = orderedEdges[0:i] + [[g[graph_nodes_keys][single_node_vertex_keys],graph_nodes_keys,single_node_vertex_keys]] + orderedEdges[i:len(orderedEdges)]
    print(orderedEdges)

    k=0
    while k < len(orderedEdges):

        node = orderedEdges.pop(0)
        # avoid cycles
        if node[1] not in mts:
            mts[node[1]]=[[node[2],node[0]]]
        else:
            mts[node[1]].append([node[2],node[0]])
        
        if node[2] not in mts:
            mts[node[2]]=[[node[1],node[0]]]
        else:
            mts[node[2]].append([node[1],node[0]])
        k+=1
        
    print(mts)

kruskal(g,1)


