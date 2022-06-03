#https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev=chars[0]
        count=1
        #starring from index 1
        i=1
        ln=len(chars)
        ans=[]
        while i<ln:
            current=chars[i]
            if current==prev:
                count+=1
            else:
                #new char found
                ans.append(prev)
                print(prev,count)
                if count>1:
                    s=str(count)
                    for x in s:
                        ans.append(x)
                
                #rename to the new char
                prev=current
                count=1
            i+=1
        ans.append(prev)
        if count>1:
            s=str(count)
            for x in s:
                ans.append(x)
                
        print(ans)
        chars.clear()
        for x in ans:
            chars.append(x)
        return len(chars)
        
                    
                
            