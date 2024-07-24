#given an space seperated integer list.find the average of elements present in the even index
mylist=list(map(int,input().split()))
sum=0
count=0
n=len(mylist)
for i in range(len(mylist)):
           if(mylist[i]/2==0):
        
             sum+=mylist[i]
           count+=1
average=sum/count
print(average)