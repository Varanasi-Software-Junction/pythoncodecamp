class Digit:
    def __init__(self,n):
        self.n = n


        self.count =0
        i=self.n
        while i!=0:
            i=i//10
            self.count +=1

    def __iter__(self):
        self.i = self.n
        self.icount =self.count
        return self
    def __next__(self):

        if self.i == 0:
            raise StopIteration
        res = self.i // (10**(self.icount-1))
        self.i = self.i%(10**(self.icount-1))
        self.icount -=1
        return res

d=Digit(56474)
for i in d:
    print(i)