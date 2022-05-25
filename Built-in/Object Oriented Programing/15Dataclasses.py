from dataclasses import dataclass, field
from typing import Any


@dataclass(init=True, repr=True, eq=True, frozen=False, order=False, unsafe_hash=False)  # Frozen make class immutable;
class Person:
    # __slots__ = ['first_name', 'second_name', 'age', 'id']  slots class cannot have default values
    first_name: str = field(default='<Undefined')
    second_name: Any = field(default='Undefined>')  # Accept all type of values
    age: int = 0, field(repr=False)  # Don't show the attribute in representation
    id: int = field(default=256)  # Set default value

    def __post_init__(self):
        self.fullName = f'{self.first_name} {self.second_name}'

    def greeting(self):
        print(fr"(\n) Hello! I'm {self.fullName}")




kv = Person('Kevin', 'Emmanuel', 14, 123)
kv2 = Person('Kevin', 'Emmanuel', 14)

print(kv)  # call the __repr__
print(kv == kv2)  # call the __eq__

kv.greeting()


@dataclass  # Slots class; Slots optimize memory and time
class SlotPerson:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float
