def attack(rows, cols, y, x, qno):
    if qno <= 1:
        return False
    if rows[qno] == y and cols[qno] == x:
        return True


rows = [0,1, 0, 0, 0, 0, 0, 0, 0]
cols= [0,1, 0, 0, 0, 0, 0, 0, 0]


y=2
x=3
qno=2
if not attack(rows,cols,y,x,2):
