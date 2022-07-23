
def printSteps(n,s,h,d):
    if n==0:
        return 0

    #move the top ones to auxiliary
    before  = printSteps(n-1,s,d,h)
    print("{} to {}".format(s,d))
    #move back to destination
    after = printSteps(n-1,h,s,d)
    return before+1+after
def main():
    s,h,d="Source","Helper","Destination"
    n=int(input("Enter the number of disks : "))
    #print the steps
    ans=printSteps(n,s,h,d)
    print("Number of Steps Taken is {}".format(ans))


if __name__ == '__main__':
    main()