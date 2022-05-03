#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s=[]
        for x in nums:
            s.append(x)

        s.sort()
        print(nums,s)
        m=0
        n=len(nums)-1
        
        p=0
        q=len(s)-1
        
        while m<=n and p<=q:
            print (m,n)
            if nums[m]==s[p] and nums[n]==s[q]:
                #compare to the soryed array
                m=m+1
                n=n-1
                p=p+1
                q=q-1
            
            elif nums[m]==s[p] and nums[n]!=s[q]:
                m=m+1
                p=p+1
            elif nums[m]!=s[p] and nums[n]==s[q]:
                n=n-1
                q=q-1
            else: #when both unequal
                return n-m+1
        
        return 0
            
                
        