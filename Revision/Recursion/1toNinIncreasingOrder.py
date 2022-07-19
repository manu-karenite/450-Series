class Solution:
    def __init__(self,num):
        self.num=num

    def printIncreasing(self):
        if self.num==1:
            print(self.num,end=" ")
            return
        
        self.num-=1
        self.printIncreasing()
        self.num+=1
        print(self.num,end=" ")


def main():
    n=int(input("Enter the Value of N: "))
    obj=Solution(n)
    obj.printIncreasing()

if __name__=="__main__":
    main()