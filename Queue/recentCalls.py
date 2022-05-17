#https://leetcode.com/problems/number-of-recent-calls/

import bisect
class RecentCounter:

    def __init__(self):
        lis=[]
        self.lis=lis
        

    def ping(self, t: int) -> int:
        self.lis.append(t)
        #print(self.lis)
        low=t-3000
        high=t
        
        #get left index 
        lindex=bisect_left(self.lis,low)
        rindex=bisect_right(self.lis,high)
        #print(self.lis,t,lindex,rindex)
        return (rindex-lindex)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
