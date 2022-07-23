from itertools import combinations
class Solution:
    def __init__(self,val):
        self.val=(val)
        self.n=len(val)

    def findSubset(self):
        #using combinations
        a=[]
        for i in range(0,self.n+1):
            a+=list(map(list,list(combinations(self.val,i))))
        #print(a)
        t=[]
        for x in a:
            t.append("".join(x))
        print(t)

        



def main():
    s=input()
    obj=Solution(s)
    obj.findSubset()
if __name__ =="__main__":
    main()