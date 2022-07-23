from itertools import combinations
class Solution:
    def __init__(self,val):
        self.val=(val)
        self.n=len(val)

    def findSubset(self,arr):
        
        if len(arr)==0:
            return [[]]
        
        letter=arr[0]
        
        ans=self.findSubset(arr[1:])
        
        #recusrion brought
        t=[]
        t=t+ans
        for x in ans:
            #each x is list itself
            z=[]
            for t1 in x:
                z.append(t1)
            z.append(letter)
            t.append(z)
        print(letter,ans,t)
        return t
        #print(arr)


def main():
    s=input()
    obj=Solution(list(s))
    ans=obj.findSubset(list(s))
    print(ans)

if __name__ =="__main__":
    main()