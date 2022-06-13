#https://leetcode.com/problems/find-players-with-zero-or-one-losses/submissions/
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        for x in matches:
            win,lose=x[0],x[1]
            #win karega usme kya add karna hai
            if lose in d:
                d[lose]+=1
            else:
                d[lose]=1
        print(d)
        winners=[]
        for x in matches:
            if x[0] not in d:
                winners.append(x[0])
        print(winners)
        
        losers=[]
        for x in d:
            d[x]==1 and losers.append(x)
        print(losers)
        s=set()
        t=set()
        for x in winners:
            s.add(x)
        for y in losers:
            t.add(y)
        print(s,t)
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        return [s,t]