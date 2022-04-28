#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        
        
        ans=[]
        #we have atleast two now
        intervals.append([10**6,10**6])
        intervals.sort()
        print(intervals)
        s=intervals[0][0]
        e=intervals[0][1]
        
        i=0
        while i<len(intervals)-1:
            print(s,e)
            if e<intervals[i+1][0]:
                print("appending")
                ans.append([s,e])
                s=intervals[i+1][0]
                e=intervals[i+1][1]
                i=i+1
                
            else:
                e=max(intervals[i][1],max(intervals[i+1][1],e))
                i=i+1
        return(ans)
                
                
        