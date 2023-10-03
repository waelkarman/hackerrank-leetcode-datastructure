class MyQueue:

    def __init__(self):
       self.s1 = [] 
       self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if(self.empty()):
            return
        return self.s1.pop(0)

    def peek(self) -> int:
        if(self.empty()):
            return
        return self.s1[0]
        

    def empty(self) -> bool:
        if(len(self.s1)==0):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
