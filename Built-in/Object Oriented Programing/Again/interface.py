from _collections_abc import Container, Sized as abc_container 


class Container:
    def __init__(self, c) -> None:
        self.c = c
    def __contains__(self, v):  # Container protocol
        return v in list(self.c)
    def __len__(self):  # Sized protocol
        return len(self.c)

    
c = Container([1,2,3])
print(issubclass(Container, abc_container))
