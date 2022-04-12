class Currency:
    def __next__(self):
        self.n+=1
        if self.n>10:
            raise StopIteration
        return self.n

    def __iter__(self):
        self.n=1
        return self
    def manage(self, n):
        if n<10:
            return "0{0}".format(n)
        return "{0}".format(n)
    def __init__(self,rs,paise):
        self.n=1
        self.total = rs * 100 + paise
    def __str__(self):
        r = self.total // 100
        p = self.total % 100
        r=self.manage(r)
        p=self.manage(p)
        return "₹ {0}.{1}".format(r, p)
    def __add__(self, other):
        return Currency(0,self.total + other.total)
    def __gt__(self, other):
        return  self.total>other.total

c1 = Currency(1,12)
c2 = Currency(10,12)
print(c1)
print(c2)
sum = c1 + c2
print(sum)
if c1>c2:
    print(c1)
else:
    print(c2)
for x in c1:
    print(x)