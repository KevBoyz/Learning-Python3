class iter1:
    def __init__(self, seq):
        self.seq = seq
        self.i = -1

    def __getitem__(self, pos):
        return self.seq[pos]

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        try:
            return self.seq[self.i]
        except IndexError:
            self.reset()
            raise StopIteration

    def __setitem__(self,i, val):
        try:
            self.seq[i] = val
        except IndexError:
            raise StopIteration
    
    def __str__(self) -> str:
        return str(self.seq)

    def reset(self):
        self.i = -1


i1 = iter1([1,2,3,4,5])
#print(i1[0])  # getitem call

for i, v in enumerate(i1):  # iter/next call
    i1[i] = v*2
i1 = [v **2 for v in i1]  # for comprehensions

print(i1)
