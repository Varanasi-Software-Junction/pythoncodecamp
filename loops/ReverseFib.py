""" Problem statement: You are given two consecutive Fibonacci Numbers and you have
to calculate the series in reverse.
For example a =34, b=21,
then
a       b       c=a-b
34      21      13
21      13      8
13      8       5
8       5       3
5       3       2
3       2       1
2       1       1
1       1       0

Observe the sequence
1. Set a=34
2. Set b=21
3. Set c=a-b
4. a=b # b of previous state becomes a of current state
5. b=c # c of previous state becomes b of new state.
6. Go back to step 3 till c becomes zero

"""
a, b = 34, 21
print(a, b, end=" ")
c = a - b
while c > 0:
    print(c, end=" ")
    a = b
    b = c
    c = a - b
print(c, end=" ")
