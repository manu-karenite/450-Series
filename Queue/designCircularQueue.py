#https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.lis=[]
        self.size=k
        self.curr=0
        

    def insertFront(self, value: int) -> bool:
        if self.curr<self.size:
            self.lis.insert(0,value)
            self.curr+=1
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if self.curr<self.size:
            self.lis.append(value)
            self.curr+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.curr==0:
            return False
        else:
            x=self.lis[0]
            self.lis=self.lis[1:]
            self.curr-=1
            return True
            
            
        

    def deleteLast(self) -> bool:
        if self.curr==0:
            return False
        else:
            x=self.lis[self.curr-1]
            self.lis=self.lis[0:self.curr-1]
            self.curr-=1
            return True
            
        

    def getFront(self) -> int:
        if self.curr==0:
            return -1
        else:
            return self.lis[0]
        

    def getRear(self) -> int:
        if self.curr==0:
            return -1
        else:
            return self.lis[self.curr-1]
        

    def isEmpty(self) -> bool:
        return self.curr==0
        

    def isFull(self) -> bool:
        return self.curr==self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()