
# MIN Heap build over an array

class HeapPriorityQueue:

    def __init__(self):
        self.array = []
        self.last = 0

    def add_value(self,val):
        self.array.append(val)
        #bubbling
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

        # bubbling with the min of the sons
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

    def print(self):
        print("Heap:")
        for a in self.array:
            print(a,end="-")
        print("")


obj=HeapPriorityQueue()
obj.add_value(29)
obj.print()
obj.add_value(30)
obj.print()
obj.add_value(28)
obj.print()
obj.add_value(40)
obj.print()
obj.add_value(5)
obj.print()
print(f"Popped: {obj.pop_value()}")
obj.print()