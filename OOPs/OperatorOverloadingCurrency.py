class Currency:
    def manage(self,n):
        if n//10 ==0:
            return "0{0}".format(n)
        return "{0}".format(n)
    def __add__(self,other):
        return Currency(0,self.total + other.total)
    def __sub__(self,other):
        return Currency(0,self.total - other.total)
    def __mul__(self,a):
        return Currency(0,a*self.total)
    def __eq__(self, other):
        return self.total == other.total
    def __gt__(self,other):
        return self.total > other.total
    def __lt__(self,other):
        return self.total < other.total
    def __ge__(self,other):
        return not self < other

    def __init__(self, rupee , paise):
        self.total= rupee*100+paise


    def __str__(self):
        r = (self.total)//100
        p = (self.total)%100
        r = self.manage(r)
        p = self.manage(p)
        return "₹{0}.{1}".format(r,p)

m = Currency(10,50)
n=4
m1 = Currency(11,50)
print(m)
print(m1)
sum = m + m1

print(sum)
sub= m-m1
print(sub)
if m1>=m:
    print('yes')
else:
    print('No')
total = m*4
print(total)
