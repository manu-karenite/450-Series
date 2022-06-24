#https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices=[]
        for x in nums1:
            y=nums2.index(x)
            indices.append(y)
        print(indices)
        
        fin=[]
        for x in indices:
            base=nums2[x]
            
            temp=nums2[x+1:]
                        
            #print(base,temp)
            ans=-1
            for y in temp:
                if y>base:
                    fin.append(y)
                    ans=1
                    break
                    
                    #continue
            if ans==-1:
                fin.append(-1)
        return fin