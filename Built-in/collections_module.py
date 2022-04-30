import collections as clt
from random import randint

cache_values = clt.deque()


def cache(func):
    def wrapper(*args):
        cache_values.append(args)
        return func(*args)
    return wrapper


@cache
def sum(x, y):
    return x + y


# print(sum(5, 5), cache_values)
# print(sum(10, 20), cache_values)


Person = clt.namedtuple('Person', ["name", "age", "gender"])

kevin = Person('Kevin', 15, 'Male')
viper = Person('Viper', randint(1, 20), 'Female')
xanes = Person('Xanes', '-x', 'Male')


# print(kevin.name)
# print(kevin._asdict())

people = [kevin, xanes, viper]
people_by_sex = clt.defaultdict(list)
for name, age, sex in people:
    people_by_sex[sex].append((name, age))  # Creates a new key and append values
print(people_by_sex)

letter_counter = clt.defaultdict(int)
for letter in 'sukablyat':
    letter_counter[letter] += 1
print(letter_counter)

print(clt.Counter('missisipi'))
print(clt.Counter([1, 1, 1, 2, 2, 3]))

people_deque = clt.deque(people)
people_deque.appendleft(Person('Chaash', 70, 'Male'))  # Efficient addition
people_deque.extend([1, 2, 3])
print(people_deque)
print(people_deque.count(kevin))



