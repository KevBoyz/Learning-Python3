class Client:
    def __init__(self, name, surname) -> None:
        self.name = name 
        self.surname = surname
        self._full_name = f'{name} {surname}'

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, obj):
        if isinstance(obj, str):
            self._full_name = obj
        else:
            raise ValueError('The value needs to be a string')

c = Client('Kev', 'Boyz')
print(c._full_name)
