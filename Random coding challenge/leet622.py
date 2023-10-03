class MyCircularQueue:

    def __init__(self, k: int):
        self._buffersize = k
        self._deque = [None] * self._buffersize
        self._front = 0
        self._contains = 0
        self._back = 1

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self._deque[self._front % self._buffersize]=value
        self._front += 1
        self._contains += 1
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        self._back -= 1
        self._deque[(self._buffersize - (self._back)) % self._buffersize] = None
        self._contains -= 1
        return True

    def Front(self) -> int:
        if(self._deque[(self._buffersize - (self._back-1)) % self._buffersize] is not None):
            return self._deque[(self._buffersize - (self._back-1)) % self._buffersize]
        else:
            return -1

    def Rear(self) -> int:
        if(self._deque[(self._front-1) % self._buffersize] is not None):
            return self._deque[(self._front-1) % self._buffersize]
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


CircQueue = MyCircularQueue(3)
print(CircQueue.enQueue(1) ) # return True
print(CircQueue.enQueue(2) ) # return True
print(CircQueue.enQueue(3) ) # return True
print(CircQueue.enQueue(4) ) # return False
print(CircQueue.Rear()     ) # return 3
print(CircQueue.isFull()   ) # return True
print(CircQueue.deQueue()  ) # return True
print(CircQueue.enQueue(4) ) # return True
print(CircQueue.Rear()     ) # return 4            