#https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], rk: str, rv: str) -> int:
        count=0
        for item in items:
            t,c,n=item[0],item[1],item[2]
            print(t,c,n)
            if (rk=="type" and rv==t) or (rk=="color" and rv==c) or (rk=="name" and rv==n):
                count=count+1
        return count
        