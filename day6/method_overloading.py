class cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return sum
#take inputs:
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))