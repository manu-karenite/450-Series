#https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    
    def addToMap(self,d,p,q):
        
        if p in d:
            temp=d[p]
            temp.append(q)
            d[p]=temp
        else:
            d[p]=[q]
            
        if q in d:
            temp=d[q]
            temp.append(p)
            d[q]=temp
        else:
            d[q]=[p]
            
    def gotPath(self,d,source,destination,s):
        s.remove(source)
        
        if source==destination:
            return True
        
        #1) check for the direct edge
        adjacent=d[source] #adjacent is the map
        if destination in adjacent:
            return True
        
        for nodes in adjacent:
            if nodes in s:
                ans=self.gotPath(d,nodes,destination,s)
                if ans:
                    #source - nodes and nodes-destination:
                    return True
            #remove set
            
            
        return False
        
        
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges)==0:
            return True
        s=set()
        d={}
        for x in edges:
            p=x[0]
            q=x[1]
            self.addToMap(d,p,q)
            s.add(p)
            s.add(q)
        print(d)
        
        
        ans=self.gotPath(d,source,destination,s)
        return ans