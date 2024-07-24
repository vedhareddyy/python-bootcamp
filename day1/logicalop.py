'''age=int(input("enter the age")) 
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("two and four wheeler")
else:
    print("two,four and six wheeler")'''

'''#problem statement solution:
napples=int(input("number of apples to buy"))
nbananas=int(input("number of bananas to buy"))
dozen=12
noranges=int(input("number of oranges to buy"))
cost_apples=15
cost_bananas=4
cost_oranges=5
amount=700
if (napples*cost_apples)+(nbananas*dozen*cost_bananas)+(noranges*cost_oranges) <= amount :
    print("the boy isnt cheated")
else:
    print("the boy got cheated")'''


'''#problem statement solution:
number=int(input("enter a number"))
if (number%2==0) and (number>0):
    print("number is even and positive")
elif (number%2!=0) and (number>0):
    print("number is odd and positive")
elif (number%2==0) and (number<0):
    print("number is even and negative")
else:
    print("number is odd and negative")'''

#mister z is selected for olympics participating in swimming competition , mister x
# and mister y are z friends,,,x is badminton...y is tabletennis...a/c to selection commitee...
# badminton players are 1)height 140cm 2)factors of 2 3)bodyfat<12%
#a/c to selection commitee.. requirements for taletennis are
#1)height min=118cm tp 148cm
#2)weight=factors of number of medals won by z
#3)bodyfast=14%,
#a/c to previous history,z participated in 14 games... out of which he is having 
#success of 65%. write a program whether x,y,z travels in the same plane or not
x_height=int(input("height elegibilty for badminton"))
x_weight=int(input("weight elegibilty for badminton"))
x_bodyfat=int(input("bodyfat elegibilty for badminton"))
y_height=int(input("height elegibilty for tabletennis"))
zmedals=(50/100)*14
y_weights=int(input("weight elegibilty for tabletennis"))
y_bodyfat=int(input("bodyfat elegibilty for tabletennis"))
if (x_height>=140) and (x_weight%2==0) and (x_bodyfat<12):
    if(y_height>118 or y_height<=148) and y_weight%zmedals==0 and y_bodyfat==14:
        print("x,y,z are travelling in same plane")
    else:
        print("only x,z are travelling in same plane")
else:
    print("only z is travelling i the plane")