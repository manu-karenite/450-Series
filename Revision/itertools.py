from itertools import permutations,combinations,pairwise
class A:
    
    def __init__(self):
        pass
    def permut(self,arr):
        lis=list(map(list,list(permutations(arr))))
        print(lis)

    def comb(self,arr):
        a=[]
        for i in range(1,len(arr)+1):
            a+=list(map(list,list(combinations(arr,i))))
        print(a)
    def pw(self,arr):
        a=pairwise(arr)
        print(a)
def main():
    arr=list(map(int,input().split(" ")))
    obj=A()
    #print permutations
    obj.permut(arr)
    obj.comb(arr)
    obj.pw(arr)

    

if __name__ == '__main__':
    main()