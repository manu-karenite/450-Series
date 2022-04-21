#https://leetcode.com/problems/lemonade-change/

class Solution:
    def check10Change(self,map):
        if 5 in map:
            value=map[5]
            map[5]=value-1
            if value==1:
                map.pop(5)
            return True
        else:
            return False
        
    def check20Change(self,map):
        #we need to return 15
        #10*1 + 5*1 or 5*3
        
        if 10 in map and 5 in map:
            value=map[10]
            if value==1:
                map.pop(10)
            else:
                map[10]=value-1
            
            value=map[5]
            if value==1:
                map.pop(5)
            else:
                map[5]=value-1
            
            
            return True
        
        if (5 in map):
            #check whether we have 3 fives
            value=map[5]
            if value<3:
                return False
            else:
                if value==3:
                    map.pop(5)
                else:
                    map[5]=value-3
                return True
            
        return False
        
   
        
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={}
        for x in bills:
            #add to counter
            if x in dic:
                dic[x]=dic[x]+1
            else:
                dic[x]=1
            print(dic)
            if x==5:
                random=1
            elif x==10:
                ans=self.check10Change(dic)
                if ans==False:
                    return False
                
            else:
                ans=self.check20Change(dic)
                if ans==False:
                    return False
            print(dic)
            
        return True
        