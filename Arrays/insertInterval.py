#https://leetcode.com/problems/insert-interval/

class Solution:
    def byStart(self,lis):
        return lis[0]
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        temp=intervals
        temp.append(newInterval)
        
        if len(temp)<=1:
            return temp
        temp.append([10**6,10**6])
        #else
        temp.sort(key=self.byStart)
        print(temp)
        
        #we have atleast two elements now
        i=0
        s=temp[0][0]
        e=temp[0][1]
        ans=[]
        while i<len(temp)-1:
            #will run accordingly
            print(s,e)
            if e<temp[i+1][0]:
                #we can end the session
                ans.append([s,e])
                print("changed",i)
                print(temp[i+1])
                s=temp[i+1][0]
                e=temp[i+1][1]
                
                i=i+1
            else:
                #need to overlap
                e=max(temp[i+1][1],max(e,temp[i][1]))
                i=i+1
        return(ans)
                
        
        
        