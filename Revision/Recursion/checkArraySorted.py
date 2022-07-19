class Solution:
    def __init__(self,arr):
        self.arr=arr


    def check(self):
        if len(self.arr)<=1:
            return True

        if self.arr[0]>self.arr[1]:
            return False
        
        self.arr=self.arr[1:]
        return (True and self.check())
def main():
    s=[int(x) for x in input("Enter the numbers : ").split(" ")]
    obj=Solution(s)
    ans=obj.check()
    if ans:
        print("{} is Sorted".format(s))
    else:
        print("{} is not Sorted!".format(s))
    


if __name__ == '__main__':
    main()