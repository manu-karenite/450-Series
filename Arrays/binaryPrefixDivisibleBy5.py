#https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums=[str(x) for x in nums]
        ans=[]
        i=0
        while i<len(nums):
            st=nums[:i+1]
            #st=[str(x) for x in st]
            num="".join(st)
            #print(num)
            x=int(num,2)
            if x%5==0:
                ans.append(True)
            else:
                ans.append(False)
            i+=1
        return ans