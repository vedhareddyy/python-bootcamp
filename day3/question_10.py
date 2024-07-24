#find the maximum element in the given list
'''test case: 0
12 23 36 44 45 57
57
--------------------------
test case:1
56 78 -8 12 34 -99
78
----------------------------'''
'''my_list=list(map(int,input().split(" ")))
max=0
for i in range(len(my_list)):
    if(max<my_list[i]):
        max=my_list[i]
print("the maximum elemrnt in the list is:",max)'''

# find the minimum element in the given list
'''my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(len(my_list)):
    if(min>my_list[i]):
        min=my_list[i]
print("the minimum element in the list is:",min)'''


#replace the elements in an array with average of min and amx elements
my_list=list(map(int,input().split(" ")))
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
print(min)
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]  
print(max)
avg=(min+max)//2
print(avg)
for i in range(len(my_list)):
     my_list=avg
print(my_list)      
        
    