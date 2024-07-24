#find the element present in k+N index
'''k=3
N=2
3 6 8 61 2
OP: 2
------------------
k=3
N=4
80 70 54 36 72
OP: Error '''

#my_list=list(map(int,input().split()))
#k=int(input())
#n=int(input())
#t=k+n
#if(len(my_list)<k+n):
#    print("error")
#else:
   #for i in range(len(my_list)):
          #print(my_list[t])
          #break
   

#print the element in the particular k index
my_list=(input( ))
k=int(input())
for i in range(my_list):
     print(k%len(my_list))      
     break    

idx=k%len(my_list)
print(my_list[idx])
