#https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for x in image:
            rev=x[::-1]
            rev=[1 if x==0 else 0 for x in rev]
            ans.append(rev)
        return ans
        
        