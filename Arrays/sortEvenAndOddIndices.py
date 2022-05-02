#https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i,x in enumerate(nums):
            if i%2==0:
                even.append(x)
            else:
                odd.append(x)
        even.sort()
        odd.sort(reverse=True)
        print(odd,even)
        
        #generalise for even based array
        ans=[]
        for i,item in enumerate(even):
            ans.append(item)
            if i==len(odd):
                pass
            else:
                ans.append(odd[i])
        
        # #append if any is remaining
        # if len(even)!=len(odd):
        #     ans.append(even[-1])
        return(ans)
            
            
            
        