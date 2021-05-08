from dataclasses import dataclass, field


@dataclass(init=True, repr=True, eq=True, frozen=False, order=True, unsafe_hash=False)  # Frozen make class immutable;
class Person:
    first_name: str
    second_name: any
    age: int = field(repr=False)  # Don't show the attribute in representation

    def __post_init__(self):
        self.fullName = f'{self.first_name} {self.second_name}'





kv = Person('Kevin', 'Emmanuel', 14)
kv2 = Person('Kevin', 'Emmanuel', 14)

print(kv)  # call the __repr__
print(kv == kv2)  # call the __eq__
