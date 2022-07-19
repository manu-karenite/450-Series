class Solution:

    def __init__(self):
        pass

    def fibonacci(self,n):
        if n==1 or n==2:
            return n-1
        
        #otherwise
        a=self.fibonacci(n-1)
        b=self.fibonacci(n-2)
        return a+b


def main():
    n=int(input("Enter the nth term you want to have : "))
    obj=Solution()
    ans=obj.fibonacci(n)
    print("The term number {} is {}".format(n,ans))
if __name__=="__main__":
    main()

