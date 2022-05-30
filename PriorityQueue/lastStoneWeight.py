#https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        
        heapq.heapify(stones)
        print(stones)
        while len(stones)>1:
            last=heapq.nsmallest(2,stones)
            [big,small]=[-last[0],-last[1]]
            if big==small:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                diff=big-small
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones,-diff)
        print(stones)
        
        if len(stones)==1:
            return -stones[0]
        else:
            return 0
            
            
        
        
        