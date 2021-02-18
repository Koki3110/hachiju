import matplotlib.pyplot as plt
o = 20  # orichin
r = 70  # range
a = 0.5
b_a = 0.5
c_b_a = 0.5
d_nc_b_a = 0.5
e_nd_nc_b_a = 0.5
c_nb_a = 0.5
d_c_nb_a = 0.5
e_nd_c_nb_a = 0.5
d_nc_nb_a = 0.5
e_d_nc_nb_a = 0.5
e_nd_nc_nb_a = 0.5
b_na = 0.5
c_b_na = 0.5
d_c_b_na = 0.5
e_nd_c_b_na = 0.5
d_nc_b_na = 0.5
e_d_nc_b_na = 0.5
e_nd_nc_b_na = 0.5
c_nb_na = 0.5
d_c_nb_na = 0.5
e_d_c_nb_na = 0.5
e_nd_c_nb_na = 0.5
d_nc_nb_na = 0.5
e_d_nc_nb_na = 0.5

for i in range(1000):
    a = min(1, (o + b_a * (c_b_a * (r/2 * b_a + r/2 * c_b_a)
                           + (1 - c_b_a) * (d_nc_b_a * (r/2 * b_a + r/2 * d_nc_b_a + o / 3)
                                            + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * b_a + r/2 * e_nd_nc_b_a + 2 * o / 3)
                                                                + (1 - e_nd_nc_b_a) * (r * b_a + 3*o/2))))
                + (1 - b_a) * (c_nb_a * (d_c_nb_a * (r/2 * c_nb_a + r/2 * d_c_nb_a + o / 3)
                                         + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * c_nb_a + r/2 * e_nd_c_nb_a + 2 * o / 3)
                                                             + (1 - e_nd_c_nb_a) * (r * c_nb_a + 3*o/2)))
                               + (1 - c_nb_a) * ((d_nc_nb_a) * (e_d_nc_nb_a *
                                                                (r/2 * d_nc_nb_a + r/2 *
                                                                 e_d_nc_nb_a + 2 * o / 3)
                                                                + (1 - e_d_nc_nb_a) * (r * d_nc_nb_a + 3*o/2))
                                                 + (1 - d_nc_nb_a) * (e_nd_nc_nb_a * (r * e_nd_nc_nb_a + 3*o/2)
                                                                      + (1 - e_nd_nc_nb_a) * 4*o))))
            / ((2*r) * (1 - (1 - b_a) * (1 - c_nb_a) * (1 - d_nc_nb_a) * (1 - e_nd_nc_nb_a))))
    b_a = min(1, (o + c_b_a * (r/2 * a + r/2 * c_b_a)
                  + (1 - c_b_a) * (d_nc_b_a * (r/2 * a + r/2 * d_nc_b_a + o / 3)
                                   + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * a + r/2 * e_nd_nc_b_a + 2 * o / 3)
                                                       + (1 - e_nd_nc_b_a) * (r * a + 3*o/2)))) / (2*r))
    c_b_a = min(1, (o + r/2 * a + r/2 * b_a) / (2*r))
    d_nc_b_a = min(1, (o + r/2 * a + r/2 * b_a + o / 3) / (2*r))
    e_nd_nc_b_a = min(1, (o + r/2 * a + r/2 * b_a + 2 * o / 3) / (2*r))
    c_nb_a = min(1, (o + d_c_nb_a * (r/2 * a + r/2 * d_c_nb_a + o / 3)
                     + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * a + r/2 * e_nd_c_nb_a + 2 * o / 3)
                                         + (1 - e_nd_c_nb_a) * (r * a + 3*o/2))) / (2*r))
    d_c_nb_a = min(1, (o + r/2 * a + r/2 * c_nb_a + o / 3) / (2*r))
    e_nd_c_nb_a = min(1, (o + r/2 * a + r/2 * c_nb_a + 2 * o / 3) / (2*r))
    d_nc_nb_a = min(1, (o + e_d_nc_nb_a * (r/2 * a + r/2 * e_d_nc_nb_a + 2 * o / 3)
                        + (1 - e_d_nc_nb_a) * (r * a + 3*o/2)) / (2*r))
    e_d_nc_nb_a = min(1, (o + r/2 * a + r/2 * d_nc_nb_a + 2 * o / 3) / (2*r))
    e_nd_nc_nb_a = min(1, (o+r*a+3*o/2)/(2*r))
    b_na = min(1, (o+c_b_na*(d_c_b_na*(r/2*c_b_na+r/2*d_c_b_na+o/3)+(1-d_c_b_na)*(e_nd_c_b_na *
                                                                                  (r/2 * c_b_na + r/2 * e_nd_c_b_na + 2 * o / 3) + (1 - e_nd_c_b_na) * (r * c_b_na + 3*o/2))) + (1 - c_b_na) * (d_nc_b_na * (e_d_nc_b_na * (r/2 * d_nc_b_na + r/2 * e_d_nc_b_na + 2 * o / 3) + (1 - e_d_nc_b_na) * (r * d_nc_b_na + 3*o/2)) + (1 - d_nc_b_na) * (e_nd_nc_b_na * (r * e_nd_nc_b_na + 3*o/2) + (1 - e_nd_nc_b_na) * 4*o))) / ((2*r) * (1 - (1 - c_b_na) * (1 - d_nc_b_na) * (1-e_nd_nc_b_na))))
    c_b_na = min(1, (o+d_c_b_na*(r/2*b_na+r/2*d_c_b_na+o/3)+(1-d_c_b_na)*((e_nd_c_b_na) *
                                                                          (r/2 * b_na + r/2 * e_nd_c_b_na + 2 * o / 3) + (1 - e_nd_c_b_na) * (r * b_na + 3*o/2))) / (2*r))
    d_c_b_na = min(1, (o + r/2 * b_na + r/2 * c_b_na + o/3) / (2*r))
    e_nd_c_b_na = min(1, (o + r/2 * b_na + r/2 * c_b_na + 2 * o / 3) / (2*r))
    d_nc_b_na = min(1, (o + e_d_nc_b_na * (r/2 * b_na + r/2 * e_d_nc_b_na + 2 * o / 3) +
                        (1 - e_d_nc_b_na) * (r * b_na + 3*o/2)) / (2*r))
    e_d_nc_b_na = min(
        1, (o + r/2 * b_na + r/2 * d_nc_b_na + 2 * o / 3) / (2*r))
    e_nd_nc_b_na = min(1, (o + r * b_na + 3*o/2) / (2*r))
    c_nb_na = min(1, (o + d_c_nb_na * (e_d_c_nb_na * (r/2 * d_c_nb_na + r/2 * e_d_c_nb_na + 2 * o / 3) + (1-e_d_c_nb_na) * (r*d_c_nb_na+3*o/2)) + (1 - d_c_nb_na) * (e_nd_c_nb_na *
                                                                                                                                                                     (r * e_nd_c_nb_na + 3*o/2) + (1 - e_nd_c_nb_na) * 4*o)) / ((2*r) * (d_c_nb_na + (1 - d_c_nb_na) * e_nd_c_nb_na)))
    d_c_nb_na = min(1, (o + e_d_c_nb_na * (r/2 * c_nb_na + r/2 * e_d_c_nb_na + 2 * o / 3) +
                        (1 - e_d_c_nb_na) * (r * c_nb_na + 3*o/2)) / (2*r))
    e_d_c_nb_na = min(1, (o + r/2 * c_nb_na + r/2 *
                          d_c_nb_na + 2 * o / 3) / (2*r))
    e_nd_c_nb_na = min(1, (o + r * c_nb_na + 3*o/2) / (2*r))
    d_nc_nb_na = min(1, (o + e_d_nc_nb_na * (r * e_d_nc_nb_na + 3*o/2) +
                         (1 - e_d_nc_nb_na) * 4 * o) / ((2*r) * e_d_nc_nb_na))
    e_d_nc_nb_na = min(1, (o+r*d_nc_nb_na+3*o/2)/(2*r))

print('a =', a)
print('b_a =', b_a)
print('c_b_a =', c_b_a)
print('d_nc_b_a =', d_nc_b_a)
print('e_nd_nc_b_a =', e_nd_nc_b_a)
print('c_nb_a =', c_nb_a)
print('d_c_nb_a =', d_c_nb_a)
print('e_nd_c_nb_a =', e_nd_c_nb_a)
print('d_nc_nb_a =', d_nc_nb_a)
print('e_d_nc_nb_a =', e_d_nc_nb_a)
print('e_nd_nc_nb_a =', e_nd_nc_nb_a)
print('b_na =', b_na)
print('c_b_na =', c_b_na)
print('d_c_b_na =', d_c_b_na)
print('e_nd_c_b_na =', e_nd_c_b_na)
print('d_nc_b_na =', d_nc_b_na)
print('e_d_nc_b_na =', e_d_nc_b_na)
print('e_nd_nc_b_na =', e_nd_nc_b_na)
print('c_nb_na =', c_nb_na)
print('d_c_nb_na =', d_c_nb_na)
print('e_d_c_nb_na =', e_d_c_nb_na)
print('e_nd_c_nb_na =', e_nd_c_nb_na)
print('d_nc_nb_na =', d_nc_nb_na)
print('e_d_nc_nb_na =', e_d_nc_nb_na)

ABC = a * b_a * c_b_a
ABD = a * b_a * (1 - c_b_a) * d_nc_b_a
ABE = a * b_a * (1 - c_b_a) * (1-d_nc_b_a) * e_nd_nc_b_a
AB = a * b_a * (1 - c_b_a) * (1 - d_nc_b_a) * (1 - e_nd_nc_b_a)
ACD = a * (1 - b_a) * c_nb_a * d_c_nb_a
ACE = a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * e_nd_c_nb_a
AC = a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * (1-e_nd_c_nb_a)
ADE = a * (1 - b_a) * (1 - c_nb_a) * d_nc_nb_a * e_d_nc_nb_a
AD = a * (1 - b_a) * (1 - c_nb_a) * d_nc_nb_a * (1-e_d_nc_nb_a)
AE = a * (1 - b_a) * (1 - c_nb_a) * (1-d_nc_nb_a) * e_nd_nc_nb_a
A = a * (1 - b_a) * (1 - c_nb_a) * (1-d_nc_nb_a) * (1-e_nd_nc_nb_a)
BCD = (1 - a) * (b_na) * c_b_na * d_c_b_na
BCE = (1 - a) * (b_na) * c_b_na * (1-d_c_b_na) * e_nd_c_b_na
BC = (1 - a) * (b_na) * c_b_na * (1-d_c_b_na) * (1-e_nd_c_b_na)
BDE = (1 - a) * (b_na) * (1 - c_b_na) * d_nc_b_na * e_d_nc_b_na
BD = (1 - a) * (b_na) * (1 - c_b_na) * d_nc_b_na * (1-e_d_nc_b_na)
BE = (1 - a) * (b_na) * (1 - c_b_na) * (1-d_nc_b_na) * e_nd_nc_b_na
B = (1 - a) * (b_na) * (1 - c_b_na) * (1-d_nc_b_na) * (1-e_nd_nc_b_na)
CDE = (1 - a) * (1 - b_na) * c_nb_na * d_c_nb_na * e_d_c_nb_na
CD = (1 - a) * (1 - b_na) * c_nb_na * d_c_nb_na * (1-e_d_c_nb_na)
CE = (1 - a) * (1 - b_na) * c_nb_na * (1-d_c_nb_na) * e_nd_c_nb_na
C = (1 - a) * (1 - b_na) * c_nb_na * (1-d_c_nb_na) * (1-e_nd_c_nb_na)
DE = (1 - a) * (1 - b_na) * (1-c_nb_na) * d_nc_nb_na * e_d_nc_nb_na
D = (1 - a) * (1 - b_na) * (1 - c_nb_na) * d_nc_nb_na * (1 - e_d_nc_nb_na)
E = (1 - a) * (1 - b_na) * (1-c_nb_na) * (1-d_nc_nb_na)
print("ABC=", ABC)
print("ABD=", ABD)
print("ABE=", ABE)
print("AB =", AB)
print("ACD=", ACD)
print("ACE=", ACE)
print("AC =", AC)
print("ADE=", ADE)
print("AD =", AD)
print("AE =", AE)
print("A  =", A)
print("BCD=", BCD)
print("BCE=", BCE)
print("BC =", BC)
print("BDE=", BDE)
print("BD =", BD)
print("BE =", BE)
print("B  =", B)
print("CDE=", CDE)
print("CD =", CD)
print("CE =", CE)
print("C  =", C)
print("DE =", DE)
print("D  =", D)
print("E  =", E)
hitori = A + B + C + D + E
sashi = AB + AC + AD + AE + BC + BD + BE + CD + CE + DE
print("一人勝ち:", hitori)
print("サシ勝負:", sashi)
print("三人勝負:", 1 - hitori - sashi)
print("D追い込まれ:", ABC)
print("E追い込まれ:", ABC + ABD + ACD + BCD)

eva = -o * (1 - a)\
    + a * (b_a * (c_b_a * (r/2 * b_a + r/2 * c_b_a - r * a)
                  + (1 - c_b_a) * (d_nc_b_a * (r/2 * b_a + r/2 * d_nc_b_a - r * a + o / 3)
                                   + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * b_a + r/2 * e_nd_nc_b_a - r * a + 2 * o / 3)
                                                       + (1 - e_nd_nc_b_a) * (r * b_a - r * a + 3*o/2))))
           + (1 - b_a) * (c_nb_a * (d_c_nb_a * (r/2 * c_nb_a + r/2 * d_c_nb_a - r * a + o / 3)
                                    + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * c_nb_a + r/2 * e_nd_c_nb_a - r * a + 2 * o / 3)
                                                        + (1-e_nd_c_nb_a)*(r*c_nb_a-r*a+3*o/2)))
                          + (1 - c_nb_a) * (d_nc_nb_a * (e_d_nc_nb_a * (r/2 * d_nc_nb_a + r/2 * e_d_nc_nb_a - r * a + 2 * o / 3)
                                                         + (1 - e_d_nc_nb_a) * (r * d_nc_nb_a - r * a + 3*o/2))
                                            + (1 - d_nc_nb_a) * (e_nd_nc_nb_a * (r * e_nd_nc_nb_a - r * a + 3*o/2)
                                                                 + (1 - e_nd_nc_nb_a) * 4*o))))
evb = a * (-o * (1 - b_a)
           + b_a * (c_b_a * (r/2 * a + r/2 * c_b_a - r * b_a)
                    + (1 - c_b_a) * (d_nc_b_a * (r/2 * a + r/2 * d_nc_b_a - r * b_a + o / 3)
                                     + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * a + r/2 * e_nd_nc_b_a - r * b_a + 2 * o / 3)
                                                         + (1 - e_nd_nc_b_a) * (r * a - r * b_a + 3*o/2)))))\
    + (1-a)*(b_na * (c_b_na*(d_c_b_na*(r/2*c_b_na+r/2*d_c_b_na-r*b_na+o/3)+(1-d_c_b_na)*(e_nd_c_b_na*(r/2*c_b_na+r/2*e_nd_c_b_na-r*b_na+2 * o / 3)+(1-e_nd_c_b_na)*(r*c_b_na-r*b_na+3*o/2)))+(1-c_b_na) *
                     (d_nc_b_na*(e_d_nc_b_na*(r/2*d_nc_b_na+r/2*e_d_nc_b_na-r*b_na+2 * o / 3)+(1-e_d_nc_b_na)*(r*d_nc_b_na-r*b_na+3*o/2))+(1-d_nc_b_na)*(e_nd_nc_b_na*(r*e_nd_nc_b_na-r*b_na+3*o/2)+(1-e_nd_nc_b_na)*4*o))) + (1-b_na)*(-o))
evc = a * b_a * (-o * (1 - c_b_a) + c_b_a * (r/2 * a + r/2 * b_a - r * c_b_a))\
    + a * (1 - b_a) * (-o * (1 - c_nb_a) + c_nb_a * (d_c_nb_a * (r/2 * a + r/2 * d_c_nb_a - r * c_nb_a + o / 3)
                                                     + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * a + r/2 * e_nd_c_nb_a - r * c_nb_a + 2 * o / 3)
                                                                         + (1 - e_nd_c_nb_a) * (r * a - r * c_nb_a + 3*o/2))))\
    + (1 - a) * (b_na * (c_b_na*(d_c_b_na*(r/2*b_na+r/2*d_c_b_na-r*c_b_na+o/3)+(1-d_c_b_na)*(e_nd_c_b_na*(r/2*b_na+r/2*e_nd_c_b_na-r*c_b_na+2 * o / 3)+(1-e_nd_c_b_na)*(r*b_na-r*c_b_na+3*o/2)))+(1-c_b_na)*(-o)) + (1-b_na) * (-o*(1-c_nb_na) +
                                                                                                                                                                                                                                c_nb_na * (d_c_nb_na * (e_d_c_nb_na * (r/2 * d_c_nb_na + r/2 * e_d_c_nb_na - r * c_nb_na + 2 * o / 3) + (1 - e_d_c_nb_na) * (r * d_c_nb_na - r * c_nb_na + 3*o/2)) + (1 - d_c_nb_na) * (e_nd_c_nb_na * (r * e_nd_c_nb_na - r * c_nb_na + 3*o/2) + (1 - e_nd_c_nb_na) * (4*o)))))
evd = a * b_a * (c_b_a * 0 + (1 - c_b_a) * (-o * (1 - d_nc_b_a) + d_nc_b_a * (r/2 * a + r/2 * b_a - r * d_nc_b_a + o / 3)))\
    + a * (1 - b_a) * c_nb_a * (-o*(1-d_c_nb_a)+d_c_nb_a*(r/2*a+r/2*c_nb_a-r*d_c_nb_a+o/3))\
    + a * (1 - b_a) * (1 - c_nb_a) * (-o * (1 - d_nc_nb_a) + d_nc_nb_a * (e_d_nc_nb_a * (r/2 * a + r/2 * e_d_nc_nb_a - r * d_nc_nb_a + 2 * o / 3)
                                                                          + (1 - e_d_nc_nb_a) * (r * a - r * d_nc_nb_a + 3*o/2)))\
    + (1-a) * (b_na * (c_b_na * ((-o) * (1 - d_c_b_na) + d_c_b_na *
                                 (r/2 * b_na + r/2 * c_b_na - r * d_c_b_na+o/3)) + (1 - c_b_na) * ((-o) * (1 - d_nc_b_na) + d_nc_b_na * (e_d_nc_b_na * (r/2 * b_na + r/2 * e_d_nc_b_na - r * d_nc_b_na + 2 * o / 3) + (1 - e_d_nc_b_na) * (r * b_na - r * d_nc_b_na + 3*o/2)))) + (1-b_na) * (c_nb_na*(-o*(1-d_c_nb_na)+d_c_nb_na*(e_d_c_nb_na*(r/2*c_nb_na+r/2*e_d_c_nb_na-r*d_c_nb_na+2 * o / 3)+(1-e_d_c_nb_na)*(r*c_nb_na-r * d_c_nb_na+3*o/2))+(1-c_nb_na) * (-o*(1-d_nc_nb_na)+d_nc_nb_na*(e_d_nc_nb_na * (r*e_d_nc_nb_na-r*d_nc_nb_na+3*o/2)+(1-e_d_nc_nb_na)*(4*o))))))
eve = -eva - evb - evc - evd
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
print("evd=", evd)
print("eve=", eve)
