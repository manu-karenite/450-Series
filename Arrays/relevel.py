var=input()
var=var.split()
n=int(var[0])
m=int(var[1])
#print(m)
ones=set()

candies=input()
candies=candies.split(" ")
#print(candies)
 #candies is an array now

bools=input()
bools=bools.split(" ")

index=0
for x in bools:
    if x=="1":
        ones.add(index)
    index=index+1

candiesPossible=[]
#print(ones)

#create a sum array
summ=0
i=0
lis=[]
while i<n:
    summ=summ+int(candies[i])
    lis.append(summ)
    i=i+1


    
i=0
while i<n:
    currValue=summ[i]

    toSubtract=0
    if i>0:
        toSubtract=i-1
    
    totalC=currValue-toSubtract

    start=i
    end=i+m-1
    if n-1<end:
        end=n-1
    for x in ones:
        if int(x)<start and int(x)>end:
            currValue=currValue+candies[int(x)]
        
    candiesPossible.append(currValue)


    # j=i
    # end=i+m-1

    # temp=set()
    # while j<=end and j<n:
    #     temp.add(str(j))
    #     j=j+1
    # #print(temp,ones)
    # output_set=set()
    # for l in temp:
    #     output_set.add(int(l))
    # for l in ones:
    #     output_set.add(int(l))
    # #print(output_set)
    # val=0
    # for x in output_set:
    #     val=val+int(candies[int(x)])
    # candiesPossible.append(val)

    i=i+1
print(candiesPossible)
candiesPossible.sort(reverse=True)

print(candiesPossible[0])

