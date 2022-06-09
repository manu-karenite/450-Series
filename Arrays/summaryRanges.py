#https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        fin=[]
        start=0
        end=0
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]+1:
                end+=1
            else:
                #okay now we need to create and insert
                if start!=end:
                    ans=str(nums[start])+"->"+str(nums[end])
                    fin.append(ans)
                else:
                    ans=str(nums[start])
                    fin.append(ans)
                #reset the start and end
                start=i
                end=i
            i+=1
        if start!=end:
            ans=str(nums[start])+"->"+str(nums[end])
            fin.append(ans)
        else:
            ans=str(nums[start])
            fin.append(ans)
        return(fin)
                
                
                
        