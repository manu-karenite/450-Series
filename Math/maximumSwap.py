#https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        g=set()
        g.add(num)
        if num<10:
            return num
        
        s=str(num)
        ln=len(s)
        
        i=0
        while i<ln-1:
            
            j=i+1
            while j<ln:
                if s[i]<s[j]:
                    #we can swap and  see
                    temp=s
                    orig=temp[:i]+s[j]+temp[i+1:j]+s[i]+temp[j+1:]
                    g.add(int(orig))
                j+=1
            i+=1
        print(g)
        return max(g)
        