
class MyCircularDeque:

    def __init__(self, k: int):
        self._buffersize = k
        self._deque = [None] * self._buffersize
        self._front = 0
        self._back = 1
        self._contains = 0

    def insertFront(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self._deque[self._front % self._buffersize]=value
        self._front += 1
        self._contains += 1
        return True

    def insertLast(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self._deque[(self._buffersize - self._back) % self._buffersize]=value
        self._back += 1
        self._contains += 1
        return True

    def deleteFront(self) -> bool:
        if(self.isEmpty()):
            return False
        self._front -= 1
        self._deque[self._front % self._buffersize] = None
        self._contains -= 1
        return True

    def deleteLast(self) -> bool:
        if(self.isEmpty()):
            return False
        self._back -= 1
        self._deque[(self._buffersize - (self._back)) % self._buffersize] = None
        self._contains -= 1
        return True


    def getFront(self) -> int:
        if(self._deque[(self._front-1) % self._buffersize] is not None):
            return self._deque[(self._front-1) % self._buffersize]
        else:
            return -1

    def getRear(self) -> int:
        if(self._deque[(self._buffersize - (self._back-1)) % self._buffersize] is not None):
            return self._deque[(self._buffersize - (self._back-1)) % self._buffersize]
        else:
            return -1

    def isEmpty(self) -> bool:
        if(self._contains > 0):
            return False
        else:
            return True

    def isFull(self) -> bool:
        if(self._contains == self._buffersize):
            return True
        else:
            return False

    def printL(self):
        print("------------------------")
        for a in self._deque:
            print(a)
        print("------------------------")



k=4
obj = MyCircularDeque(k)
print(obj.insertFront(9))
print(obj.deleteLast())
print(obj.getRear())
print(obj.getFront())
print(obj.getFront())
print(obj.deleteFront())
print(obj.insertFront(6))
print(obj.insertLast(5))
print(obj.insertFront(9))
print(obj.getFront())
print(obj.insertFront(6))

obj.printL()
