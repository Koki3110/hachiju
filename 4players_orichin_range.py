import matplotlib.pyplot as plt
o = 20  # orichin
r = 70  # range

a = 0.5
b_a = 0.5
c_b_a = 0.5
d_nc_b_a = 0.5
c_nb_a = 0.5
d_c_nb_a = 0.5
d_nc_nb_a = 0.5
b_na = 0.5
c_b_na = 0.5
d_c_b_na = 0.5
d_nc_b_na = 0.5
c_nb_na = 0.5
d_c_nb_na = 0.5

for i in range(1000):
    a = (o+b_a*(c_b_a*(r/2*b_a+r/2*c_b_a)+(1-c_b_a)*(d_nc_b_a *
                                                     (r/2 * b_a + r/2 * d_nc_b_a + o / 3) + (1 - d_nc_b_a) * (r * b_a + o))) + (1 - b_a) * (c_nb_a * (d_c_nb_a * (r/2 * c_nb_a + r/2 * d_c_nb_a + o / 3) + (1 - d_c_nb_a) * (r * c_nb_a + o)) + (1 - c_nb_a) * (d_nc_nb_a * (r * d_nc_nb_a + o) + (1 - d_nc_nb_a) * 3*o))) / ((2*r) * (1 - (1 - b_a) * (1-c_nb_a) * (1 - d_nc_nb_a)))
    b_a = (o+c_b_a*(r/2*a+r/2*c_b_a)+(1-c_b_a)*((d_nc_b_a) *
                                                (r/2 * a + r/2 * d_nc_b_a + o / 3) + (1 - d_nc_b_a) * (r * a + o))) / (2*r)
    c_b_a = (o + r/2 * a + r/2 * b_a) / (2*r)
    d_nc_b_a = (o + r/2 * a + r/2 * b_a + o / 3) / (2*r)
    c_nb_a = (o + d_c_nb_a * (r/2 * a + r/2 * d_c_nb_a + o / 3) +
              (1 - d_c_nb_a) * (r * a + o)) / (2*r)
    d_c_nb_a = (o + r/2 * a + r/2 * c_nb_a + o / 3) / (2*r)
    d_nc_nb_a = (o + r * a + o) / (2*r)
    b_na = (o + c_b_na * (d_c_b_na * (r/2 * c_b_na + r/2 * d_c_b_na + o / 3) + (1-d_c_b_na) * (r*c_b_na+o)) + (1 - c_b_na) * (d_nc_b_na *
                                                                                                                              (r * d_nc_b_na + o) + (1 - d_nc_b_na) * 3*o)) / ((2*r) * (c_b_na + (1 - c_b_na) * d_nc_b_na))
    c_b_na = (o + d_c_b_na * (r/2 * b_na + r/2 * d_c_b_na + o / 3) +
              (1 - d_c_b_na) * (r * b_na + o)) / (2*r)
    d_c_b_na = (o + r/2 * b_na + r/2 * c_b_na + o / 3) / (2*r)
    d_nc_b_na = (o + r * b_na + o) / (2*r)
    c_nb_na = (o + d_c_nb_na * (r * d_c_nb_na + o) +
               (1 - d_c_nb_na) * 3*o) / ((2*r) * d_c_nb_na)
    d_c_nb_na = (o+r*c_nb_na+o)/(2*r)

print("a =", a)
print("b_a =", b_a)
print('c_b_a =', c_b_a)
print('d_nc_b_a =', d_nc_b_a)
print('c_nb_a =', c_nb_a)
print('d_c_nb_a =', d_c_nb_a)
print('d_nc_nb_a =', d_nc_nb_a)
print('b_na =', b_na)
print('c_b_na =', c_b_na)
print('d_c_b_na =', d_c_b_na)
print('d_nc_b_na =', d_nc_b_na)
print('c_nb_na =', c_nb_na)
print('d_c_nb_na =', d_c_nb_na)

ABC = a * b_a * c_b_a
ABD = a * b_a * (1 - c_b_a) * d_nc_b_a
AB = a * b_a * (1 - c_b_a) * (1-d_nc_b_a)
ACD = a * (1 - b_a) * c_nb_a * d_c_nb_a
AC = a * (1 - b_a) * c_nb_a * (1-d_c_nb_a)
AD = a * (1 - b_a) * (1 - c_nb_a) * d_nc_nb_a
A = a * (1 - b_a) * (1 - c_nb_a) * (1-d_nc_nb_a)
BCD = (1 - a) * (b_na) * c_b_na * d_c_b_na
BC = (1 - a) * (b_na) * c_b_na * (1-d_c_b_na)
BD = (1 - a) * (b_na) * (1 - c_b_na) * d_nc_b_na
B = (1 - a) * (b_na) * (1 - c_b_na) * (1-d_nc_b_na)
CD = (1 - a) * (1 - b_na) * c_nb_na * d_c_nb_na
C = (1 - a) * (1 - b_na) * c_nb_na * (1-d_c_nb_na)
D = (1 - a) * (1 - b_na) * (1-c_nb_na)
print("ABC=", ABC)
print("ABD=", ABD)
print("AB =", AB)
print("ACD=", ACD)
print("AC =", AC)
print("AD =", AD)
print("A  =", A)
print("BCD=", BCD)
print("BC =", BC)
print("BD =", BD)
print("B  =", B)
print("CD =", CD)
print("C  =", C)
print("D  =", D)
print("一人勝ち:", A + B + C + D)
print("サシ勝負:", AB + AC + AD + BC + BD + CD)
print("三人勝負:", ABC + ABD + ACD + BCD)
print("D追い込まれ:", ABC)

eva = -o*(1-a) + a * (b_a*(c_b_a*(r/2*b_a+r/2*c_b_a-r*a)+(1-c_b_a)*(d_nc_b_a*(r/2*b_a+r/2*d_nc_b_a-r*a+o/3)+(1-d_nc_b_a)*(r*b_a-r*a+o)))+(1-b_a) *
                      (c_nb_a*(d_c_nb_a*(r/2*c_nb_a+r/2*d_c_nb_a-r*a+o/3)+(1-d_c_nb_a)*(r*c_nb_a-r*a+o))+(1-c_nb_a)*(d_nc_nb_a*(r*d_nc_nb_a-r*a+o)+(1-d_nc_nb_a)*3*o)))
evb = a * (b_a*(c_b_a*(r/2*a+r/2*c_b_a-r*b_a)+(1-c_b_a)*(d_nc_b_a*(r/2*a+r/2*d_nc_b_a-r*b_a+o/3)+(1-d_nc_b_a)*(r*a-r*b_a+o)))+(1-b_a)*(-o)) + (1-a) * (-o*(1-b_na) +
                                                                                                                                                       b_na*(c_b_na*(d_c_b_na*(r/2*c_b_na+r/2*d_c_b_na-r*b_na+o/3)+(1-d_c_b_na)*(r*c_b_na-r*b_na+o))+(1-c_b_na)*(d_nc_b_na*(r*d_nc_b_na-r*b_na+o)+(1-d_nc_b_na)*(3*o))))
evc = a * (b_a * ((-o) * (1 - c_b_a) + c_b_a *
                  (r/2 * a + r/2 * b_a - r * c_b_a)) + (1 - b_a) * ((-o) * (1 - c_nb_a) + c_nb_a * (d_c_nb_a * (r/2 * a + r/2 * d_c_nb_a - r * c_nb_a + o / 3) + (1 - d_c_nb_a) * (r * a - r * c_nb_a + o)))) + (1-a) * (b_na*(-o*(1-c_b_na)+c_b_na*(d_c_b_na*(r/2*b_na+r/2*d_c_b_na-r*c_b_na+o/3)+(1-d_c_b_na)*(r*b_na-r * c_b_na+o))+(1-b_na) * (-o*(1-c_nb_na)+c_nb_na*(d_c_nb_na * (r*d_c_nb_na-r*c_nb_na+o)+(1-d_c_nb_na)*(3*o)))))
evd = -eva - evb - evc
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
print("evd=", evd)
