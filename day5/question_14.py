#strings: string methods are is alpha,is digit,is alpha numeric,is upper,is lower,
#converting into lower,converting into upper case,title case,swap case

#str="   hello world    "
#print(str.lower())
#print(str.upper())
#print(str.title())
#print(str.capitalize())
#print(str.swapcase())
#print(str.strip())
#print(str.replace('a','2'))
#print(str.split())
#print(str.split('a'))

#inp="helloworld"
#print(inp.isalpha())
#print(inp.isnumeric())
#print(inp.isalnum())
#print(inp.islower())
#print(inp.isupper())
#print(inp.istitle())
#print(inp.isdigit())
 
#ascii values
#print(ord('c'))
#using ascii values
#print(chr(90))

#check how many vowels are present in a string
'''str=input()
vowels="aeiouAEIOU"
count=0
for char in str:
    if char in vowels:
     count+=1
print("the number of vowels:",count)'''

#write a program to print all the count of consonents
'''vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
   if(i in vowels):
      count+=1
for i in inp:
   if(i in consonents):
      print("number of consonents:",count)

#OR
str=input()
consonents="bcdfghjklmnpqrstvwxyz"
count=0
for char in str:
   if char in consonents:
      count+=1
print("the number of consonents:",count)'''
      
#print all the vowels followed by consonents
'''vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
   if(i in vowels):
    ans+=i
for i in inp:
   if(i in consonents):
      ans+=i
print(ans)'''
   
 #print the non reapeating/unique elements  
'''vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
   if(i not in ans):
      ans+=i
print(ans)'''

#print the sum of digits in a string
'''a=input()
sum=0
for i in a:
   if(ord(i))>=48 and (ord(i))<=57:
      sum=sum+int(i)
print("the sum is:" +str(sum))'''

#reverse the number present in a given string

#print the ascii values
'''for i in range(0,128):
    print(chr(i),end=" ")

for i in range(32,128):
    print(chr(i),end=" ")'''


#for i in range(32,128):
 #   print(chr(i),end=" ")

'''inp=input()
count=0
for i in(inp):
    if (ord(i)>=48 and ord(i)<=57):
      count+=int(i)
print(count)'''

#write a code to print all the capital letters in a given string
'''or i in range(65,91):
  print(chr(i),end=" ")'''

#remove all the brackets from the given algebraic expression
'''inp=input()
for i  in (inp):
     if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==125 or ord(i)==123):
      pass
     else:
        print(i,end=" ")
print()'''

#print the next coming four letters with the addition of 4 EXAMPLE ABC GIVES DEF
'''s=input()
n=int(input())
for i in s:
    e=ord(i)+n
    print(chr(e),end="")'''


#try it with xyz same as above#

# print hello-----world
'''s=input()
new=" "
count=0
for i in s:
    if(i=="-"):
        count+=1
    else:
        new+=i
print("-"*count+new)'''



'''for i in range(5):
    for j in range(5):
        print("*",end="")
    print()'''

#range
for i in range(10):
    for j in range(10):
        if(i==j):
            print(" ",end="")
        else:
            print("*",end="")
    print()
