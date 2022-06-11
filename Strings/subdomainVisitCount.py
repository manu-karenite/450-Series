#https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        for x in cpdomains:
            r=x.split(" ")
            freq,website=int(r[0]),r[1]
            #print(freq)
            #print(website)
            
            s=website.split(".")
            s1=[]
            if len(s)==2:
                s1=[s[-1],s[-2]+"."+s[-1]]
                
                
            elif len(s)==3:
                s1=[s[-1],s[-2]+"."+s[-1],s[-3]+"."+s[-2]+"."+s[-1]]
                
            print(s1)
            for x in s1:
                #print(x,freq)
                if x in d:
                    d[x]+=freq
                else:
                    d[x]=int(freq)
            print(d)
        ans=[]
        for z in d:
            ans.append(str(d[z])+" "+z)
        return(ans)
            
        