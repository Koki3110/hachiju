import matplotlib.pyplot as plt
o = 20  # orichin
r = 70  # range
a = 0.5
b = 0.5

for i in range(1000):
    a = (o + r * b * b + o * (1-b))/(2*r*b)
    b = (o + r * a)/(2*r)
print("a=", a)
print("b=", b)
print("AB =", a * b)
print("A  =", a * (1-b))
print("B  =", 1 - a)
print("一人勝ち:", 1 - a * b)
print("サシ勝負:", a * b)
eva = -o * (1 - a) + a * (b * r * (b - a) + o * (1 - b))
evb = -eva
print("eva=", eva)
print("evb=", evb)
