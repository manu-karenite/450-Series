#https://leetcode.com/problems/map-sum-pairs/

class MapSum:

    def __init__(self):
        d={}
        self.d=d
        

    def insert(self, key: str, val: int) -> None:
        self.d[key]=val
        

    def sum(self, prefix: str) -> int:
        s=0
        for x in self.d:
            if prefix in x and x.index(prefix)==0:
                s+=self.d[x]
        return s
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)