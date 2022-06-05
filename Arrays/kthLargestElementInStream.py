#https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #always maintain an array of k integers only
        self.lis=nums
        self.lis.sort()
        self.lis=self.lis[::-1]
        self.lis=self.lis[0:k]
        self.lis=self.lis[::-1]
        #print(self.lis)
        self.k=k
        
        
        

    def add(self, val: int) -> int:
        if len(self.lis)<self.k:
            self.lis.append(val)
            self.lis.sort()
            return self.lis[0]
        
        if val<=self.lis[0]:
            #dont do anything
            return self.lis[0]
        
        if val>=self.lis[-1]:
            self.lis.pop(0)
            self.lis.append(val)
            return self.lis[0]
        
        if val>self.lis[0] and val<self.lis[-1]:
            self.lis.append(val)
            self.lis.sort()
            self.lis.pop(0)
            #print("return",self.lis)
            return self.lis[0]
            
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)