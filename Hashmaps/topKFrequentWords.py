#https://leetcode.com/problems/top-k-frequent-words/

#https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for x in words:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        print(d)
        
        l={}
        for x in d:
            if d[x] in l:
                temp=l[d[x]]
                temp.append(x)
                l[d[x]]=temp
                
                
            else:
                l[d[x]]=[x]
        print(l)
        
        fin=[]
        for x in l:
            z=l[x]
            z.sort()
            fin.append([x,z])
        print(fin)
        fin.sort(reverse=True)
        m=[]
        for x in fin:
            m+=x[1]
        return m[0:k]
                
            
                
        