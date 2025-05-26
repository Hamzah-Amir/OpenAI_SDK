from typing import Generic, TypeVar,ClassVar
from dataclasses import dataclass, field
# Example of Generic Dataclass
T =TypeVar("T")
@dataclass
class Lst(Generic[T]):
    items:list[T] = field(default_factory=list)
    limit:ClassVar[int] = 3

    def add(self, item:T):
        return self.items.append(item)
    def remove(self, item:T):
        return self.items.pop(item)

list1 = Lst[int]()
print(list1)
list1.add(50)
list1.add(60)
print(list1)
list1.remove(1)
print(list1)
list1.remove(0)
print(list1)
print("\n-------String example-------\n")
string = Lst[str]()
string.add("Hamza")
string.add("Amir")
string.add("Sana")
print(string)
print(string.remove(0))
print(string)