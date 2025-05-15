#OOP CONCEPTS...
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
class Student():
    def __init__(self, name:str, marks: int)->None:
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"{self.name} scored {self.marks} marks...")
        
student_detail = Student("samiya", 90) 
student_detail.display()     



#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
class Counter():
    count: int = 0
    
    def __init__(self):
       Counter.count +=1
    @classmethod
    
    def display_count(cls):
        print(f"total objects = {cls.count}")
        
obj1 = Counter()
obj2 = Counter()        
Counter.display_count()


#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car():
    def __init__(self, brand: str)->None:
        self.brand = brand
    def start(self):
            print(f"{self.brand}")
            my_car = Car("Toyota")

my_car = Car("Toyota")
print(my_car.brand)
my_car.start()


#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
class Bank():
    bank_name = "HBL"
    def __init__(self)->None:
        pass
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name    
        
    def show(self):
        print(f"{self.bank_name}")

bank1 = Bank()
bank2 = Bank()

bank1.show()  
bank2.show()  


Bank.change_bank_name("National Bank")

bank1.show()  
bank2.show()    


#Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils():
    @staticmethod
    def add(a, b):
        return f"sum of {a} and {b} is {a+b}"
    
print(MathUtils.add(2, 4))    


#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger():
    def __init__(self):
        print("constructor is created")
        
    def __del__(self):
        print("constructor is destructor")
        
log = Logger()
del log            

#Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.
class Employee():
    def __init__(self,name, salary, ssn):
        self.name = name
        self._salary = salary      #protected variable
        self.__ssn = ssn            #private variable
        
salary = Employee("abc",14000, 20000)
print(salary.name)
print(salary._salary)  
print(salary._Employee__ssn)       
     
     
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
class Person():
    def __init__(self, name):
        self.name = name
        print(f"name is {self.name}")
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)        
        self.subject = subject
        print(f"subject is {self.subject}")
        
t = Teacher("ayat", "maths")           

#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
        def __init__(self, height, width) -> None:
            self.height = height
            self.width = width
            
        def area(self):
            return self.width * self.height    
        
result = Rectangle(5, 6)
print(result.area())        


#Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog():
    def __init__(self , name, breed) -> None:
        self.name = name
        self.breed = breed
        
    def bark(self):
         print(f"{self.name} the {self.breed} says: Woof! Woof!")  
        
dog = Dog("tommy", "pug")
dog.bark()   


#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book():
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
Book.increment_book_count()
Book.increment_book_count()        
print("total books = " , Book.total_books)        

#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConvertor():
    @staticmethod
    def celsius_to_fahrenheit(c):
        fahrenheit =  (9/5 * c) + 32
        return fahrenheit
    
print(TemperatureConvertor.celsius_to_fahrenheit(80))   


#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
class Engine():
    def start(self):
        print("engine has started....")
        
class Car():
    def __init__(self, engine) -> None:
        self .engine = engine
       
        
    def start(self):
         print("car is ready to start")
         self.engine.start() 
         
engine = Engine()
car = Car(engine)         
car.start()

#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, emplyee_id):
        self.name = name
        self.emplyee_id = emplyee_id
        
    def show_detail(self):
        print(f"emplyee ID: {self.emplyee_id}, and name: {self.name}")
            
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee
        
    def show_department(self):
        print(f"department: {self.department_name}")  
        self.employee.show_detail()        
        
emplyee = Employee("sara", 201)
depart = Department("HR", emplyee)
depart.show_department()             

# ------------------------------------------


#Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A():
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("class B")      
        
class C(A):
    def show(self):
        print("class C")        
        
class D(B, C):
    pass          
    
d = D()
d.show()
print(D.__mro__)       #method resolution order


#Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def main():
        print("function is called")
        return func()
    return main

@log_function_call
def say_hello():
    print("hello")
 
say_hello()    


#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
def add_greeting(cls):
    def greet(self):
        return "hello..."
    cls.greet = greet
    return cls

@add_greeting
class Person():
    def __init__(self, name):
        self.name = name
        
person = Person("Ali")  
print(person.greet())  


