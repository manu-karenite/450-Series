#https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s=set()

        count=1
        
        for x in arr:
            ct=arr.count(x)
            if ct==1:
                if count==k:
                    return x
                else:
                    count=count+1
        return ""
        
        