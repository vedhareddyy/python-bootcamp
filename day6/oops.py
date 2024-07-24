class myclass:
    def add(a,b):
        return(a+b)
    def sub(a,b):
        return(a-b)
    def mul(a,b):
        return(a*b)
    def div(a,b):
        return(a/b)
    def mod(a,b):
        return(a%b)
obj1=myclass
obj2=myclass
print(obj1.add(45,89))
print(obj1.sub(45,99))
print(obj1.mul(45,89))
print(obj1.div(48,9))
print(obj1.mod(45,89))
print(obj2.add(499,89))
print(obj2.sub(499,89))
print(obj2.mul(40,890))
print(obj2.div(56,8))
print(obj2.mod(12,4))
