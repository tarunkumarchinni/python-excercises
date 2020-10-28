"""
classes 
create a class that provides the factorials for the list of numbers provided. Checkout __repr__ and __str__ methods and implement those for your class."""

class Factorial:
    def __init__(self,num):
        self.num=num

    def fact(self):
        z=1
        while (self.num!=0):
            z=z*self.num
            self.num=self.num-1
        return z
x=int(input("Enter the number:"))
y=Factorial(x)
print(y.fact())
    