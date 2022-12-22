from numbers import Number

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


# Example

class Retangle:
    def __init__(self, l, a) -> None:
        self.l = l
        self.a = a

    @property  # __set__ not implemented
    def area(self):  # Read-only methods
        return self.l * self.a


r = Retangle(3,3)
#  r.area = 9  # Exeption


class PositiveNumber:
    def __init__(self):
        self._n = None
    
    def get_n(self):
        return self._n

    def set_n(self, obj):
        if not isinstance(obj, Number):
            raise TypeError(f"Can't set ({type(obj)}), only Number.")
        if obj < 0:
            raise ValueError("Can't set negative number.")
        self._n = obj  
        
    def del_n(self):
        del self._n 

    n = property(get_n, set_n, del_n)


n = PositiveNumber() 
n.n = -10
