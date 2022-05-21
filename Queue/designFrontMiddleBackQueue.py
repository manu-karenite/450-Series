#https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue:

    def __init__(self):
        self.lis=[]
        
        

    def pushFront(self, val: int) -> None:
        self.lis.insert(0,val)
        

    def pushMiddle(self, val: int) -> None:
        l=len(self.lis)
        if l%2==0:
            self.lis.insert(l//2,val)
            
        else:
            self.lis.insert(l//2,val)
        

    def pushBack(self, val: int) -> None:
        self.lis.append(val)
        

    def popFront(self) -> int:
        if len(self.lis)==0:
            return -1
        x=self.lis[0]
        self.lis=self.lis[1:]
        return x
        

    def popMiddle(self) -> int:
        l=len(self.lis)
        if l==0:
            return -1
        if l%2==0:
            i=l//2-1
            x=self.lis[i]
            self.lis=self.lis[0:i]+self.lis[i+1:]
            return x
            
            
        else:
            i=l//2
            x=self.lis[i]
            self.lis=self.lis[0:i]+self.lis[i+1:]
            return x
            

    def popBack(self) -> int:
        if len(self.lis)==0:
            return -1
            
        else:
            x=self.lis[-1]
            self.lis=self.lis[0:len(self.lis)-1]
            return x
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()