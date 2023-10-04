
# MIN Heap build over an array

class HeapPriorityQueue:

    def __init__(self, arr=[]):
        self.array = arr
        self.last = 0

    def add_value(self,val):
        self.array.append(val)
        #up bubbling swap
        i=self.last+1
        while self.array[int((i/2)-1)]>self.array[i-1]:
            tmp = self.array[i-1]
            self.array[i-1] = self.array[int((i/2)-1)]
            self.array[int((i/2)-1)]=tmp
            i = int(i/2)
        self.last+=1

    def pop_value(self):
        tmp=self.array[0]
        self.array[0]=self.array.pop()
        self.last-=1
        i=1

        # down bubbling swap with the min of the sons
        if len(self.array) > ((i*2+1)-1):  
            if self.array[(i*2)-1] > self.array[(i*2+1)-1]:
                c= 1
            else:
                c= 0
        while len(self.array) > ((i*2+c)-1) and self.array[int(i-1)] > self.array[(i*2+c)-1]:
            tmp0 = self.array[(i*2+c)-1]
            self.array[(i*2+c)-1] = self.array[int(i-1)]
            self.array[int(i-1)]=tmp0
            i = int(i*2)
            if len(self.array) > ((i*2+1)-1):  
                if self.array[(i*2)-1] > self.array[(i*2+1)-1]:
                    c= 1
                else:
                    c= 0
        return tmp

    #using Heapify

    def get_the_next_node(self):
        i=len(self.array)-1
        while i >= 0:
            yield i+1
            i-=1

    def get_the_smallest_neighbors_i(self,i):
        if self.have_left_neighbor(i) and self.have_right_neighbor(i):
            if self.array[self.get_left_neighbor_index(i)-1] > self.array[self.get_right_neighbor_index(i)-1]:
                return self.get_right_neighbor_index(i)
            else:
                return self.get_left_neighbor_index(i)
        elif self.have_left_neighbor(i) and not self.have_right_neighbor(i):
            return self.get_left_neighbor_index(i)
        else:
            return -1
        

    def get_left_neighbor_index(self,i):
        return i*2
     
    def get_right_neighbor_index(self,i):
        return i*2+1

    def have_left_neighbor(self,i):
        if self.get_left_neighbor_index(i) <= len(self.array):
            return True
        else:
            return False

    def have_right_neighbor(self,i):
        if self.get_right_neighbor_index(i) <= len(self.array):
            return True
        else:
            return False

    def bubble_swap(self,a,b):
        while b > 0:
            tmp=self.array[a]
            self.array[a]=self.array[b]
            self.array[b]=tmp
            a=b
            b = self.get_the_smallest_neighbors_i(a+1)-1

    def heapify(self):
        nodes = self.get_the_next_node()
        for root in nodes: 
            son = self.get_the_smallest_neighbors_i(root)
            if son != -1 and self.array[son-1] < self.array[root-1]:
                self.bubble_swap(root-1,son-1)

    def print(self):
        print("Heap:")
        for a in self.array:
            print(a,end=" ")
        print("")

if __name__ == "__main__":
    obj=HeapPriorityQueue([29,28,30,40,5])
    #obj.add_value(29)
    #obj.print()
    #obj.add_value(30)
    #obj.print()
    #obj.add_value(28)
    #obj.print()
    #obj.add_value(40)
    #obj.print()
    #obj.add_value(5)
    #obj.print()
    #print(f"Popped: {obj.pop_value()}")
    #obj.print()

    obj.print()
    obj.heapify()
    obj.print()