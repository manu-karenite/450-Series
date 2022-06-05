
def main():

    start=input("Please enter the starting times : ").split(" ")
    end =input("Please enter the end times : ").split(" ")
    start=[int(y) for y in start]
    end=[int(y) for y in end]
    
    times=[]
    for i,x in enumerate(start):
        times.append([x,end[i]])
    

    #sort by the end times...
    times.sort(key=lambda x : x[1])
    print(times)

    ans=[]
    curr_end=times[0][1]
    ans.append(times[0])
    for x in times[1:]:
        if x[0]>=curr_end:
            #we can schedule this..
            ans.append(x)
            curr_end=x[1]

    print(ans)


if __name__=="__main__":
    main()