class Solution:
    def __init__(self,x):
        self.x=x

    def fact(self,x):
        if x<=1:
            return 1
        return x*self.fact(x-1)

def main():
    n=int(input("Enter the Number : "))
    obj=Solution(n)
    ans=obj.fact(n)
    print("Factorial of {} is {}".format(n,ans))

if __name__=="__main__":
    main()