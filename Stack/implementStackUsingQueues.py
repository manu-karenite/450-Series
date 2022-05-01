#https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    
    def __init__(self):
        self.lis=[]
        

    def push(self, x: int) -> None:
        self.lis.append(x)
        

    def pop(self) -> int:
        return self.lis.pop()
        

    def top(self) -> int:
        return self.lis[-1]
        

    def empty(self) -> bool:
        if self.lis:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()