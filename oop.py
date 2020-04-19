# %% calculator

class Calculator:
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
        
    def add(self):
        return self.value1 + self.value2
    
    def subtract(self):
        return self.value1 - self.value2

operation  = input("+ or - ? ")

first_value = float(input("Enter first number: "))
second_value = float(input("Enter second number: "))
    
c1 = Calculator(first_value, second_value)

if operation == '+':
    print(c1.add())
elif operation == '-':
    print(c1.subtract())


# %% encapsulation
    
class Student:
    def __init__(self, name, scholarship):
        self.name = name
        self.__scholarship = scholarship # private attribtue
        
    def getMoney(self):
        return self.__scholarship
    
    def setMoney(self, amount):
        self.__scholarship = amount
        
    # private method
    def __increase(self, amount):
        self.__scholarship = self.__scholarship + amount
    
    # sonra bashqa bir global metodda ishletmek olar
    def g(self, amount):
        self.__increase(amount)
        
s1 = Student("Kamran", 1000)
s2 = Student("Ali", 0)

# %% inheritance

class Human:
   def __init__(self,name,age,gender):
       print("Human is created.")
       self.name = name
       self.age = age
       self.gender = gender
    
   def talk(self):
       print("Human is talking.")
 
class Teacher(Human):
   def __init__(self, name, age, gender, university):
       print("Teacher is created")
       super().__init__(name, age, gender) # classin adi yazilsa superin yerine, initin ichinde self de qeyd olunmalidi
       self.university = university

   def getName(self):
       print(self.name)
          
t1 = Teacher("Kamran", 22, "male", "BSU")  

# %% abstract classes

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self): pass
    
    @abstractmethod
    def run(self):  pass
    
class Bird(Animal):
    def walk(self): 
        print("walk")
    def run(self): 
        print("run")

a = Bird()

# abstract classlar sadece child classlar uchun template yaradir
# abstract classlardan instance yaradila bilmez
# abstract classda yazilmish metodlar mecbui istifade olunmalidir

# %% overriding

class Animal: # parent class
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    def toString(self):
        print("monkey")
        
animal1 = Animal()
animal1.toString()

monkey1 = Monkey()
monkey1.toString() # burda metod override olundu

# %% polymorphism
# override-la eyni sheydir

class Car:
    def __init__(self):
        pass
        
    def increasePower(self):
        print("Let's increase power")
        
class Sedan(Car):
    def __init__(self, power): # ozunde olan
        super().__init__() # yuxaridan gelen
        self.power = power
        
    def increasePower(self): # polymorphism happens right here
        mount = 50
        result = self.power + (self.power * mount)
        print(result)
        

s1 = Sedan(20)
s1.increasePower()

# %% project

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
     
    # will be overrided
    def toString():
        pass

class Square(Shape):
    
    def __init__(self, edge):
        self.__edge = edge
        
    def area(self):
        area = self.__edge**2
        print("Square area: ", area)
        
    def perimeter(self):
        perimeter = self.__edge*4
        print("Square perimeter: ", perimeter)
        
    def toString(self):
        print("Edge of this square is: ", self.__edge)
    
    # def getEdge(self):
    #     return self.edge
    
    # def setEdge(self, edge):
    #     self.__edge = edge

s1 = Square(5)




















