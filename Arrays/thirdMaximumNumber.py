#https://leetcode.com/problems/third-maximum-number/

import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #create a set
        myset=set()
        
        lis=[]
        for x in nums:
            if x in myset:
                #don't add
                continue
            else:
                myset.add(x)
                lis.append(x)
        
        if len(lis)<3:
            return max(lis)
    
        #now we have atleast 3 object
        #we want the max heap
        i=0
        while i<len(lis):
            lis[i]=-lis[i]
            i=i+1
        #now heapify the max heap
        heapq.heapify(lis)
        #remove two items from the pq
        curr=heapq.heappop(lis)
        curr=heapq.heappop(lis)
        curr=heapq.heappop(lis)
        return -curr