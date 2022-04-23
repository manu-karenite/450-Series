#https://leetcode.com/problems/design-hashset/

class MyHashSet:
    lis=[]
    def __init__(self):
        self.lis=[]
        
        

    def add(self, key: int) -> None:
        if key not in self.lis:
            self.lis.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.lis:
            self.lis.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.lis
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)