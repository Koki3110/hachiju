import matplotlib.pyplot as plt
o = 20  # orichin
r = 70  # range
a = 0.5
b_a = 0.5
b_na = 0.5
c_b_a = 0.5
c_b_na = 0.5
c_nb_a = 0.5

for i in range(1000):
    a = (o + b_a * (c_b_a * (r/2 * b_a + r/2 * c_b_a) + (1-c_b_a) * (r*b_a+o/2)) + (1 - b_a) * (c_nb_a *
                                                                                                (r * c_nb_a + o/2) + (1 - c_nb_a) * 2*o)) / (2*r * (b_a + (1 - b_a) * c_nb_a))
    b_a = (o + c_b_a * (r/2 * a + r/2 * c_b_a) + (1-c_b_a)*(r*a+o/2))/(2*r)
    c_b_a = (o + r/2 * a + r/2 * b_a) / (2*r)
    c_nb_a = (o + r * a + o/2) / (2*r)
    b_na = (o+c_b_na*(r*c_b_na+o/2)+(1-c_b_na)*2*o)/(2*r*c_b_na)
    c_b_na = (o + r * b_na + o / 2) / (2 * r)

print("a=", a)
print("b_a=", b_a)
print("c_b_a=", c_b_a)
print("c_nb_a=", c_nb_a)
print("b_na=", b_na)
print("c_b_na=", c_b_na)

ABC = a * b_a * c_b_a
AB = a * b_a * (1 - c_b_a)
AC = a * (1 - b_a) * c_nb_a
A = a * (1 - b_a) * (1 - c_nb_a)
BC = (1 - a) * (b_na) * c_b_na
B = (1 - a) * (b_na) * (1 - c_b_na)
C = (1 - a) * (1 - b_na)
print("ABC=", ABC)
print("AB =", AB)
print("AC =", AC)
print("A  =", A)
print("BC =", BC)
print("B  =", B)
print("C  =", C)
print("一人勝ち:", A + B + C)
print("サシ勝負:", AB + AC + BC)
print("三人勝負:", ABC)

eva = -o * (1 - a) + a * (b_a * (c_b_a * (r/2*b_a+r/2*c_b_a-r*a)+(1-c_b_a)
                                 * (r*b_a-r*a+o/2))+(1-b_a)*(c_nb_a*(r*c_nb_a-r*a+o/2)+(1-c_nb_a)*2*o))
evb = a * (b_a*(c_b_a*(r/2*a+r/2*c_b_a-r*b_a)+(1-c_b_a)*(r*a-r*b_a+o/2))-o *
           (1-b_a))+(1-a)*(b_na*(c_b_na*(r*c_b_na-r*b_na+o/2)+(1-c_b_na)*2*o)-o*(1-b_na))
evc = -eva - evb
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
