#find the missing element in array
'''my_list=list(map(int,input().split()))
k=sum(my_list)
print("sum of list:",k)
sum=0
n=int(input("enter the number"))
sum=(n*(n+1))//2
print(f"the sum of first {n} natural numbers is",sum)
print("missing number in the list is",sum-k)'''

#find the duplicates in the array
'''my_list = list(map(int,input().split()))
print("dulicate elements in the given array:")
for i in range(0 ,len(my_list)):
    for j in range(i+1,len(my_list)):
       if(my_list[i]) == (my_list[j]):
          print(my_list[j])'''


#sum of indivual
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)'''

#find the sum of squares of a digit in a given number
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)'''

#find the sum of even number
'''n=123456
sum=0
while n>0:
    r=n%10
    if(r%2==0):
         sum=sum+r
    n=n//10
print(sum)'''


#reverse of a number
n=1234
sum=0
rev=" "
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))