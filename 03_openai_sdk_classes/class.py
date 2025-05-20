from dataclasses import dataclass
from typing import Any

#  Understanding callable in Python
@dataclass
class Human:
    name : str
    age : int

    def greet(self):
        return f"Hi, I'm {self.name}."
    
    def eat(self):
        return f'{self.name} is eating.'
print("\n--------Output of First Class--------\n")
obj1 = Human(name="Hamza", age=18)
print(obj1.name)  
print(obj1.age)
print(obj1.greet())
print(obj1.eat())

# If we will print obj1() it will show error because it is not callable
print("\n ---Calling the first class's object with parenthesis---\n")
try:
    obj1()
except Exception as e:
    print("The object is not callable")

print("\nIt return the error because we did not initialized __call__ method in class")

# Creating another Class and making it Callable
@dataclass
class Male:
    name:str
    age:int
    
    def greet(self):
        return f"Hi, I'm {self.name}."
    
    def eat(self):
        return f'{self.name} is eating.'

    # To make it callable we will __call__ function
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

print("\n---------Output of Second class---------\n")
obj2 = Male(name="Hamza",age=18)
print(obj2.name)  
print(obj2.age)
print(obj2.greet())
print(obj2.eat())
print("\n ---Calling the Second class's object with parenthesis---\n")
print(obj2()) # As wee will it now call it it will execute all methods inside the class
print("\nIt returns 'NONE' because here we initialized the__call__ but with built-in configs and pass none to func")

#  We can also ad a default message which will be shown when ever anyone calls it 

@dataclass
class Female:
    name:str
    age:int
    
    def greet(self):
        return f"Hi, I'm {self.name}."
    
    def eat(self):
        return f'{self.name} is eating.'

    # To make it callable we will __call__ function
    def __call__(self):
        #  to print a random message instead of all functions we will pass it in return
        return "Hello I am Female Class"

# lets make its instance and call it 
print("\n--------Output of Third class---------\n")
obj3 = Female(name="Maria", age=17)
print(obj3.name)  
print(obj3.age)
print(obj3.greet())
print(obj3.eat())
print("\n ---Calling the Third class's object with parenthesis---\n")
print(obj3())
print('\nAt last it returns our custom message that we initialized in the Female class')

#  We can check all maguc functions of a class object by using dir func

print("\n",obj3.__dict__) # this will wrap all data of objject in dict

"""object can be called with parenthesis if we will not add parenthesis with name of obj
it will display all data instead of __call__ function"""
print("Output of obj without parenthesis->",obj2) # without parenthesis
print("Output of  obj with parenthesis->",obj2()) # with parenthesis

# QUICK QUIZ

"""
We have added a dataclass decorator above class, when we create a instance of that class
does the class initializes itself or there is any other function or method is called through the decorator.
You can use Chat GPT for finding answer. 
"""