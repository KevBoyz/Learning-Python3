class A:
    def a(self):
        print('worked')


class B:
    def b(self):
        print('worked too')


class C(A, B):
    def c(self):
        print('Ok, all working')


c = C()

c.a()
c.b()
c.c()

