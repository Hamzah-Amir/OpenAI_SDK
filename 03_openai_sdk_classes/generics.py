#  Example without generics
from typing import TypeVar
print('------Example without generics-----')
def first_element(item:list):
    return item[0]

num =[10,5,3,6]
letter = ['g','k','o']

print(first_element(letter))
print(first_element(num))

print("----GENERIC EXAMPLE------")
# Generics Example
from typing import TypeVar
A = TypeVar("A")

def generics_first_element(item:list[A]) -> A:
    return item[0]
print(generics_first_element(num))
print(generics_first_element(letter))