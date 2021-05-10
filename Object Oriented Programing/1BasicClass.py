from datetime import datetime
import urllib.request



class Person:
    def __init__(self, name='Escravo'):
        self.name = name

    def hello(self):
        print(f'??? - Olá, me chamo {self.name}')

    def time(self):
        print(f'{self.name} - Agora são {datetime.now().time()}')

    def request(self):
        print(f'{self.name} - Digite uma url para requisitar ')
        url = str(input('> '))
        try:
            urllib.request.urlopen(url)
        except:
            print(f'Request recusada pelo servidor')
        else:
            print(f'Request aceita')


name = str(input('Digite um nome para mim: '))
if name == '':
    person = Person()
else:
    person = Person(name)

person.hello()
input()
person.time()
input()
person.request()