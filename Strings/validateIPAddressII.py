#https://leetcode.com/problems/validate-ip-address/

class Solution:
    
    def ipv4(self,q):
        ans=q.split(".")
        
        
        print(ans)
        if len(ans)!=4:
            return False
        
        #now we have 4
        ct=0
        for x in ans:
            if len(x)==0:
                return False
            if x.isnumeric()==False:
                return False
            #now it is a number
            to_int=int(x)
            print(to_int)
            if to_int<0 or to_int>255:

                return False
                
            #now check leading zeroes
            
            to_int=str(to_int)
            if len(to_int)!=len(x):
                #means zeroes were tgere
                return False
            ct+=1
        return ct==4 and True
            
        
        
        
    def ipv6(self,q):
        ans=q.split(":")
        print(ans)
        print(ans)
        if len(ans)!=8:
            return False
        #NOW WE HAVE 8 SUBSTRINGS IN IPV6 SEP[ERATED BY ] ":"
        st="0123456789abcdefABCDEF"
        ct=0
        for x in ans:
            if len(x)<1 or len(x)>4:
                return False
            try:
                l=int(x,16)
                ct+=1
            except:
                return False
        return ct==8 and True
            
        
        
    def validIPAddress(self, queryIP: str) -> str:
        
        
        ans1=False
        ans2=False
        if "." in queryIP:
            ans1=self.ipv4(queryIP)
            if ans1 or ans2:
                return "IPv4"
            else:
                return "Neither"
                
        elif ":" in queryIP:
            ans2=self.ipv6(queryIP)
            if ans1 or ans2:
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"
        