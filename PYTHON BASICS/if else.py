print("hello")

a = 1
b = 2
if a < b:
    print("a is less than b")
    print("a is definitely less than b")
print("Not sure if a is less than B")

c = 3
d = 5
if c < d:
    print("c is less than d")
elif c == d:
    print("c is equal to d")
else:
    print("c is not less than d")
print("outside the block")

g = 7
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal tto h")
    else:
        print("g is greater h")

