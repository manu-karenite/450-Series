#https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        #create a list of words having 2k characters and remaining
        lis=[]
        ans=[]
        print(len(s))
        while len(s)>0:
            if len(s)<2*k:
                lis.append(s)
                s=""
            else:
                lis.append(s[0:2*k])
                s=s[2*k:len(s)]
        print(lis)
                
        for x in lis:
            if len(x)<k:
                ans.append(x[::-1])
            else:
                ans.append(x[0:k][::-1]+x[k:len(x)])
        print(ans)
        ans="".join(ans)
        return ans
        