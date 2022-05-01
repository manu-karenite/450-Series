#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.lis=[]
        

    def push(self, x: int) -> None:
        self.lis.append(x)
        

    def pop(self) -> int:
        return self.lis.pop(0)
        

    def peek(self) -> int:
        return self.lis[0]
        

    def empty(self) -> bool:
        if self.lis:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()