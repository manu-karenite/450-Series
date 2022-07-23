class Solution:
    def __init__(self,n):
        self.n=n

    def giveStrings(self):
        if self.n<=0:
            return []
        if self.n==1:
            return ["0","1"]
        self.n-=1
        bringRemaining=self.giveStrings()
        temp=[]
        for s in bringRemaining:
            #add 0s no problems
            temp.append("0"+s)
            if s[0:1]=="0":
                temp.append("1"+s)
        return temp
         

def main():
    n=int(input("Enter the value of n : "))
    obj=Solution(n)
    ans=obj.giveStrings()
    print("There are {} valid Binary Numbers are : {}".format(len(ans),ans))
    

if __name__=="__main__":
    main()