"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(node is None):
            return None
        
        queue = {node}
        discovered = []
        l=[]
        copyg = {}
        n_list = []

        while len(queue)>0:
            current = queue.pop()
            
            discovered.append(current)

            if copyg.get(current.val) is None:
                current_c = copy.copy(current)
                copyg[current_c.val] = current_c
            else:
                current_c = copyg.get(current.val) 
            current_c.neighbors = []

            n_list.clear()
            for n in current.neighbors:
                if copyg.get(n.val) is not None:
                    if copyg[n.val] not in copyg[n.val].neighbors:
                        n_list.append(copyg[n.val])    
                else:
                    n_c = copy.copy(n)
                    n_c.neighbors = []
                    copyg[n_c.val] = n_c
                    n_list.append(copyg[n.val])
                if n not in discovered and n not in queue :
                    queue.add(n)
                
            current_c.neighbors = copy.copy(n_list)
        return copyg[1]

    def bfs(self,node):
        queue = {node}
        discovered = []
        while len(queue)>0:
            current = queue.pop()
            print(f"current: {current} - {current.val}")
            discovered.append(current)
            for n in current.neighbors:
                print(f"neighbor: {n} - {n.val} ")
                if n not in discovered:
                    queue.add(n)
