class Animal:
    def speak():
        return "Animal is speaking"
#single inh:
class Dog(Animal):
    def Bark():
        return "Bow..."
#multi inh:
class puppy(Dog):
    def puppy_speak():
        return "in puppy"
obj1=Animal
obj2=Dog
obj3=puppy
print(obj1.speak())
print(obj2.Bark())
print(obj3.puppy_speak())