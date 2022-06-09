#https://leetcode.com/problems/design-a-stack-with-increment-operation/
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxi=maxSize
        self.lis=[]
        

    def push(self, x: int) -> None:
        if len(self.lis)<self.maxi:
            self.lis.append(x)
        print("PUSHH",x,self.lis)
            
        
        

    def pop(self) -> int:
        if len(self.lis)==0:
            return -1
        key=self.lis.pop(-1)
        print("POP",key,self.lis)
        return key
        

    def increment(self, k: int, val: int) -> None:
        temp=self.lis[0:k]
        temp=[x+val for x in temp]
        self.lis=temp+self.lis[k:]
        
        print("INC",k,self.lis)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)