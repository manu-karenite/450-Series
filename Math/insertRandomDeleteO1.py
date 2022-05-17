#https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import random
class RandomizedSet:

    def __init__(self):
        s=set()
        self.s=s
        

    def insert(self, val: int) -> bool:
        ans=True
        if val in self.s:
            ans=False
        self.s.add(val)
        return ans
        

    def remove(self, val: int) -> bool:
        ans=False
        if val in self.s:
            self.s.remove(val)
            ans=True
        return ans
        

    def getRandom(self) -> int:
        x=list(self.s)
        rand=int(random()*(len(x)))
        return x[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
