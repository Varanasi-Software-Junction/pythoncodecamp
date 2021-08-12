class NumberIter:
    def __init__(self,n):
        self.n=n
        self.i=0
        l=[]
        while n>0:
            rem=n % 10
            n=n//10
            l= [rem] + l
        self.l=l
    def __iter__(self):
        self.i=0
        return self
    def __next__(self):
        if self.i>=len(self.l):
            raise StopIteration
        self.i+=1
        return self.l[self.i-1]


c=NumberIter(123)
for x in c:
    print(x)
for x in c:
    print(x)
