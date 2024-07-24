#n=int(input())
#sum=n*(n+1)//2
#print(sum)
#sort 1st half in ascending order and 2nd half in descending order4
#n=list(int(input().split(" ")))

'''my_list=list(list(map(int,input().split())))
count=0
for i in range(1,len(my_list)-1):
    if (my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]):
      count=i
if(my_list[-1]>my_list[-2] and my_list[-1]>count):
   count=len(my_list)-1
print(my_list[count])'''
'''a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
while b!=0:
    a,b=b,a%b
print("gcd of 2 numbers is: ",a)'''

'''a=int(input())
if(a==0):
    print("prime")
else:
    print("not prime")'''

#lcm
'''a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c,d=a,b
while b!=0:
    a,b=b,a%b
    print((c*d)//a)'''



'''a=int(input("enter a number: "))
r=a**0.5
count=0
if a==1:
    print("not a prime numb3r")
elif a==2:
    print("prime number")
for i in range(2,int(r+1)):
    if a%1==0:
        count=1
        break
if count==0:
    print("prime number")
else:
    print("not a prime number")'''



#write a program to print all the prime numbers in a given range
n=int(input("enter a number :"))
for i in range(2000,2025):
    if n%4==0 and n%100!=0:
        print(i)
    else:
        print("not a leap year") 

