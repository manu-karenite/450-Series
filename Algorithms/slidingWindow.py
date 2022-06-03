#to find max sum of all subarrays of k size
#input -> 2 3 4 5 6 1 90 8 7
#input K-> 3
#output -> determine 
#len of output = len(input)-k

def printAns(lis,k) -> None:
    ans=[]
    curr_maximum=sum(lis[:k])

    i=1
    while i<=len(lis)-k:
        temp=curr_maximum-lis[i-1]+lis[i+k-1]
        curr_maximum=max(curr_maximum,temp)
        i+=1
    print("Maximum of all Subarrays is : ",curr_maximum)

    
def main():
    lis=input("Please enter the elements of array : ")
    lis=lis.split(" ")
    lis=[int(x) for x in lis]
    k=int(input("Please enter value of k : "))
    if k>len(lis):
        print("Value of k above Limit!")
        return

    printAns(lis,k)

if __name__=="__main__":
    main()