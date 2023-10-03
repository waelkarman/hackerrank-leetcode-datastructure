# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self._lis = []
        self._recursive(nestedList)
        self._lis.reverse()

    def __iter__(self):
        return self

    def _recursive(self,nl):
        if(nl == []):
            return
        check_list = type(nl) is list
        if(not check_list):
            self._lis.append(nl)
        else:
            for i in nl:
                self._recursive(i)

    def __next__(self) -> int:
        return self._lis.pop()
    
    def next(self) -> int:
        return self._lis.pop()      
                
    def hasNext(self) -> bool:
        if(len(self._lis)>0):
            return True
        else:
            return False


# Your NestedIterator object will be instantiated and called as such:
nestedList = [1,[4,[6,4,3],6,[8,9]]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())

print(v)
