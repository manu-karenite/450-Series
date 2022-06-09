#https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

    
    
        arr=arr[::-1]
        maxi=max(arr)
        idx=arr.index(maxi)
        idx=len(arr)-1-idx
        arr=arr[::-1]
        l=arr[:idx+1]
        r=arr[idx:]
        print(l,r)
        
        if len(l)-1==0 or len(r)-1==0:
            return False
        if len(l)!=len(set(l)) or len(r)!=len(set(r)):
            return False
        
        #now only strictly increasig
        leftMost=l[0]
        for x in l[1:]:
            if x<=leftMost:
                return False
            leftMost=x
        
        leftMost=r[0]
        for x in r[1:]:
            if x>=leftMost:
                return False
            leftMost=x
        return True
        
        print(l,r)