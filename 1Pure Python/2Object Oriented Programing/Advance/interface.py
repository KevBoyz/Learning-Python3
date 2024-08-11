from _collections_abc import Container as abc_container, Sized, Collection, MutableSequence
from typing import Iterator


class Container(abc_container, Sized):  # Explicit implementation
    def __init__(self, c) -> None:
        self.c = c
    def __contains__(self, v):  # Container protocol
        return v in list(self.c)  # This make this class a container
    def __len__(self):  # Sized protocol
        return len(self.c)  # This make this class a sizeble

    
# c = Container([1,2,3])
# print(issubclass(Container, abc_container))


class Coleção(Collection):  # Try remove one of this methods
    def __init__(self, *c) -> None:
        super().__init__()
        self.c = c

    def __contains__(self, x: object) -> bool:
        return x in self.c
    
    def __len__(self) -> int:
        return len(self.c)

    def __iter__(self) -> Iterator:
        return self

    def __getitem__(self, i):  # This only method implements count, index, iterator
        return self.c[i]


c = Coleção(1,2,3,4,5)


class CrazyList(MutableSequence):
    ...  # Try insstanciate this

