#https://leetcode.com/problems/masking-personal-information/

class Solution:
        
    def solveEmail(self,s):
        print(s)
        name,domain=s.split("@")[0].lower(),s.split("@")[1].lower()
        print(name,domain)
        name=name[0:1]+"*****"+name[-1]
        return name+"@"+domain
    
    def solvePhone(self,s):
        tel=""
        for i in range(0,len(s),1):
            cr=s[i:i+1]
            if cr=="+" or cr=="-" or cr=="(" or cr==")" or cr==" ":
                tel=tel+""
            else:
                tel=tel+cr
        if len(tel)==10:
            return "***-***-"+tel[6:]
            
            
        elif len(tel)==11:
            return "+*-***-***-"+tel[7:]
            
        elif len(tel)==12:
            return "+**-***-***-"+tel[8:]
            
        elif len(tel)==13:
            return "+***-***-***-"+tel[9:]
            
            
    def maskPII(self, s: str) -> str:
        if "@" in s:
            ans=self.solveEmail(s)
            return ans
        else:
            ans=self.solvePhone(s)
            return ans
        