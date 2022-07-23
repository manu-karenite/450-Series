class A:
    def __init__(self,a,n):
        self.a=a
        self.n=n
    
    def calculate(self):
        if self.n==0:
            return 1
        self.n-=1
        ans=self.calculate()
        return self.a*ans



def main():
    s=input("Enter values of a and n : ").split(" ")
    a,n=int(s[0]),int(s[1])
    obj=A(a,n)
    ans=obj.calculate()
    print("Value of {}^{} is {}".format(a,n,ans))

if __name__=="__main__":
    main()
