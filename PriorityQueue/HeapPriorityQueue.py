
# MIN Heap

class HeapPriorityQueue:

    def __init__(self):
        self.array = []
        self.last = 0

    def add_value(self,val):
        self.array.append(val)
        #bubbling
        i=self.last+1
        while self.array[int((i-1)/2)]>self.array[i-1]:
            tmp = self.array[i-1]
            self.array[i-1] = self.array[int((i-1)/2)]
            self.array[int((i-1)/2)]=tmp
            i = int(i/2)
        self.last+=1

    def pop_value(self): #INCOMPLETE
        self.array.pop()

    def print(self):
        print("Heap:")
        for a in self.array:
            print(a,end="-")
        print("")


obj=HeapPriorityQueue()
obj.add_value(30)
obj.print()
obj.add_value(10)
obj.print()
obj.add_value(40)
obj.print()
obj.add_value(5)
obj.print()