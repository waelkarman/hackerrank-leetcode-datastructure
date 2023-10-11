
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        # print(len(self.q1))

    def pop(self) -> int:
        if(len(self.q1)==0):
            return

        for a in self.q1:
            self.q2.append(a)
        desired = self.q2.pop() 
        
        self.q1.clear()

        for b in self.q2:
            self.q1.append(b)
        
        self.q2.clear()
        print(len(self.q1))
        print(len(self.q2))
        return desired

    def top(self) -> int:
        for a in self.q1:
            self.q2.append(a)
        desired = self.q2.pop()
        self.q2.clear()
        return desired

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        else: 
            return False
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(1)
obj.top()
obj.pop()
obj.pop()

print(obj.empty())

# obj.push(2)
# obj.push(3)
# obj.push(4)

# param_2 = obj.pop()
# print(param_2)
# param_2 = obj.pop()
# print(param_2)
# param_2 = obj.pop()
# print(param_2)
# param_2 = obj.pop()




# param_4 = obj.empty()
# print(param_4)
