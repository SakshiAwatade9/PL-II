#OOP concepts 

#Creating a class and object
class Student():
    def show(self):
        print("Student class method")
obj = Student()
obj.show()


#Demonsrate constructor
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name: ",self.name)
s = Student("Sakshi")
s.display()


#Instance and variables
class Student:
    college = "GCE Karad"              #instance variable
    def __init__(self, name):
        self.name = name               #instance variable
s1=Student("John")
s2=Student("Alice")
print(s1.name, s1.college)
print(s2.name, s2.college)


#Single inheritance
class Parent:
    def show(self):
        print("Parent classs")
class Child(Parent):
    def display(self):
        print("Child class")
c=Child()
c.show()
c.display()


#Multiple inheritance
class A:
    def showA(self):
        print("Class A")
class B:
    def showB(self):
        print("Class B")
class C(A,B):
    pass
obj=C()
obj.showA()
obj.showB()


#Multilevel inheritance
class A:
    def showA(self):
        print("A")
class B(A):
    def showB(self):
        print("B")
class C(B):
    def showC(self):
        print("C")
        
obj=C()
obj.showA()
obj.showB()
obj.showC()


#Method Overriding
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def show(self):
        print("Child method")
obj=Child()
obj.show()


#Area of shapes using inheritance
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self, l, b):
        print("Area of Rectangle: ", l*b)
class Circle(Shape):
    def area(self, r):
        print("Area of a circle: ",3.14*r*r)
r=Rectangle()
r.area(10,5)

c=Circle()
c.area(10)


#Encapsulation
class Student:
    def __init__(self):
        self.__marks=90                           #private variable
    def get_marks(self):
        return self.__marks
s=Student()
print(s.get_marks())


#Polymorphism
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
for animal in (Dog(), Cat()):
    animal.sound()