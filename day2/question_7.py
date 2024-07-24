# you are given with a comma seperated natural numbers 1 to 10. print even numbers
'''my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list),2):
   # print(my_list[i],end=" ")
    count+=1
    print(count)'''
#how many even numbers are there in the output

#you are given with a spaced seperated integer list. find number of even elements 
#and number of odd elements in a given list
my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)


