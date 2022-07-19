class Solution:
    def __init__(self,num):
        self.num=num

    def printDecreasing(self):
        if self.num==1:
            print(self.num,end=" ")
            return
        print(self.num,end=" ")
        self.num-=1
        self.printDecreasing()
        


def main():
    n=int(input("Enter the Value of N: "))
    obj=Solution(n)
    obj.printDecreasing()

if __name__=="__main__":
    main()