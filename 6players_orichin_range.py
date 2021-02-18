import matplotlib.pyplot as plt
o = 20  # orichin
r = 70  # range
a = 0.5
b_a = 0.5
c_b_a = 0.5
d_nc_b_a = 0.5
e_nd_nc_b_a = 0.5
f_ne_nd_nc_b_a = 0.5
c_nb_a = 0.5
d_c_nb_a = 0.5
e_nd_c_nb_a = 0.5
f_ne_nd_c_nb_a = 0.5
d_nc_nb_a = 0.5
e_d_nc_nb_a = 0.5
f_ne_d_nc_nb_a = 0.5
e_nd_nc_nb_a = 0.5
f_e_nd_nc_nb_a = 0.5
f_ne_nd_nc_nb_a = 0.5
b_na = 0.5
c_b_na = 0.5
d_c_b_na = 0.5
e_nd_c_b_na = 0.5
f_ne_nd_c_b_na = 0.5
d_nc_b_na = 0.5
e_d_nc_b_na = 0.5
f_ne_d_nc_b_na = 0.5
e_nd_nc_b_na = 0.5
f_e_nd_nc_b_na = 0.5
f_ne_nd_nc_b_na = 0.5
c_nb_na = 0.5
d_c_nb_na = 0.5
e_d_c_nb_na = 0.5
f_ne_d_c_nb_na = 0.5
e_nd_c_nb_na = 0.5
f_e_nd_c_nb_na = 0.5
f_ne_nd_c_nb_na = 0.5
d_nc_nb_na = 0.5
e_d_nc_nb_na = 0.5
f_e_d_nc_nb_na = 0.5
f_ne_d_nc_nb_na = 0.5
e_nd_nc_nb_na = 0.5
f_e_nd_nc_nb_na = 0.5

for i in range(1000):
    a = min(1, (o
                + b_a * (c_b_a * (r/2 * b_a + r/2 * c_b_a)
                         + (1 - c_b_a) * (d_nc_b_a * (r/2 * b_a + r/2 * d_nc_b_a + o / 3)
                                          + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * b_a + r/2 * e_nd_nc_b_a + 2 * o / 3)
                                                              + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (r/2 * b_a + r/2 * f_ne_nd_nc_b_a + o)
                                                                                     + (1 - f_ne_nd_nc_b_a) * (r * b_a + 4 * o / 2)))))
                + (1-b_a)*(c_nb_a * (d_c_nb_a * (r/2 * c_nb_a + r/2 * d_c_nb_a + o/3)
                                     + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * c_nb_a + r/2 * e_nd_c_nb_a + 2 * o / 3)
                                                         + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (r/2 * c_nb_a + r/2 * f_ne_nd_c_nb_a + 3*o / 3)
                                                                                + (1 - f_ne_nd_c_nb_a) * (r * c_nb_a + 4 * o / 2))))
                           + (1 - c_nb_a) * (d_nc_nb_a * (e_d_nc_nb_a * (r/2 * d_nc_nb_a + r/2 * e_d_nc_nb_a + 2 * o / 3)
                                                          + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (r/2 * d_nc_nb_a + r/2 * f_ne_d_nc_nb_a + 3*o / 3)
                                                                                 + (1 - f_ne_d_nc_nb_a) * (r * d_nc_nb_a + 4 * o / 2)))
                                             + (1 - d_nc_nb_a) * ((e_nd_nc_nb_a) * (f_e_nd_nc_nb_a *
                                                                                    (r/2 * e_nd_nc_nb_a + r/2 *
                                                                                     f_e_nd_nc_nb_a + 3*o / 3)
                                                                                    + (1 - f_e_nd_nc_nb_a) * (r * e_nd_nc_nb_a + 4 * o / 2))
                                                                  + (1 - e_nd_nc_nb_a) * (f_ne_nd_nc_nb_a * (r * f_ne_nd_nc_nb_a + 4 * o / 2)
                                                                                          + (1 - f_ne_nd_nc_nb_a) * 5*o)))))
            / ((2*r) * (1 - (1 - b_a) * (1 - c_nb_a) * (1 - d_nc_nb_a) * (1 - e_nd_nc_nb_a) * (1 - f_ne_nd_nc_nb_a))))
    b_a = min(1, (o
                  + c_b_a * (r/2 * a + r/2 * c_b_a)
                  + (1 - c_b_a) * (d_nc_b_a * (r/2 * a + r/2 * d_nc_b_a + o / 3)
                                   + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * a + r/2 * e_nd_nc_b_a + 2 * o / 3)
                                                       + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (r/2 * a + r/2 * f_ne_nd_nc_b_a + 3*o / 3)
                                                                              + (1 - f_ne_nd_nc_b_a) * (r * a + 4 * o / 2))))) / (2*r))
    c_b_a = min(1, (o + r/2 * a + r/2 * b_a) / (2*r))
    d_nc_b_a = min(1, (o + r / 2 * a + r / 2 * b_a + o / 3) / (2 * r))
    e_nd_nc_b_a = min(1, (o+r/2*a+r/2*b_a+2 * o / 3)/(2*r))
    f_ne_nd_nc_b_a = min(1, (o + r/2 * a + r/2 * b_a + 3*o / 3) / (2*r))
    #
    c_nb_a = min(1, (o + d_c_nb_a * (r/2 * a + r/2 * d_c_nb_a+o/3)
                     + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * a + r/2 * e_nd_c_nb_a + 2 * o / 3)
                                         + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (r/2 * a + r/2 * f_ne_nd_c_nb_a + 3*o / 3)
                                                                + (1 - f_ne_nd_c_nb_a) * (r * a + 4 * o / 2)))) / (2*r))
    d_c_nb_a = min(1, (o + r/2 * a + r/2 * c_nb_a+o/3) / (2*r))
    e_nd_c_nb_a = min(1, (o + r/2 * a + r/2 * c_nb_a + 2 * o / 3) / (2*r))
    f_ne_nd_c_nb_a = min(1, (o + r/2 * a + r/2 * c_nb_a + 3*o / 3) / (2*r))
    d_nc_nb_a = min(1, (o + e_d_nc_nb_a * (r/2 * a + r/2 * e_d_nc_nb_a + 2 * o / 3)
                        + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (r/2 * a + r/2 * f_ne_d_nc_nb_a + 3*o / 3)
                                               + (1 - f_ne_d_nc_nb_a) * (r * a + 4 * o / 2))) / (2*r))
    e_d_nc_nb_a = min(1, (o + r/2 * a + r/2 * d_nc_nb_a + 2 * o / 3) / (2*r))
    f_ne_d_nc_nb_a = min(1, (o + r/2 * a + r/2 * d_nc_nb_a + 3*o / 3) / (2*r))
    e_nd_nc_nb_a = min(1, (o + f_e_nd_nc_nb_a * (r/2 * a + r/2 * f_e_nd_nc_nb_a + 3*o / 3)
                           + (1 - f_e_nd_nc_nb_a) * (r * a + 4 * o / 2)) / (2*r))
    f_e_nd_nc_nb_a = min(
        1, (o + r/2 * a + r/2 * e_nd_nc_nb_a + 3*o / 3) / (2*r))
    f_ne_nd_nc_nb_a = min(1, (o + r * a + 4 * o / 2) / (2*r))
    #
    b_na = min(1, (o + c_b_na * (d_c_b_na * (r/2 * c_b_na + r/2 * d_c_b_na + o/3)
                                 + (1 - d_c_b_na) * (e_nd_c_b_na * (r/2 * c_b_na + r/2 * e_nd_c_b_na + 2 * o / 3)
                                                     + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (r/2 * c_b_na + r/2 * f_ne_nd_c_b_na + 3*o / 3)
                                                                            + (1 - f_ne_nd_c_b_na) * (r * c_b_na + 4 * o / 2))))
                   + (1 - c_b_na) * (d_nc_b_na * (e_d_nc_b_na * (r/2 * d_nc_b_na + r/2 * e_d_nc_b_na + 2 * o / 3)
                                                  + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (r/2 * d_nc_b_na + r/2 * f_ne_d_nc_b_na + 3*o / 3)
                                                                         + (1 - f_ne_d_nc_b_na) * (r * d_nc_b_na + 4 * o / 2)))
                                     + (1 - d_nc_b_na) * ((e_nd_nc_b_na) * (f_e_nd_nc_b_na *
                                                                            (r/2 * e_nd_nc_b_na + r/2 *
                                                                             f_e_nd_nc_b_na + 3*o / 3)
                                                                            + (1 - f_e_nd_nc_b_na) * (r * e_nd_nc_b_na + 4 * o / 2))
                                                          + (1 - e_nd_nc_b_na) * (f_ne_nd_nc_b_na * (r * f_ne_nd_nc_b_na + 4 * o / 2)
                                                                                  + (1 - f_ne_nd_nc_b_na) * 5*o))))
               / ((2*r) * (1 - (1 - c_b_na) * (1 - d_nc_b_na) * (1 - e_nd_nc_b_na) * (1 - f_ne_nd_nc_b_na))))
    c_b_na = min(1, (o + d_c_b_na * (r/2 * b_na + r/2 * d_c_b_na+o/3)
                     + (1 - d_c_b_na) * (e_nd_c_b_na * (r/2 * b_na + r/2 * e_nd_c_b_na + 2 * o / 3)
                                         + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (r/2 * b_na + r/2 * f_ne_nd_c_b_na + 3*o / 3)
                                                                + (1 - f_ne_nd_c_b_na) * (r * b_na + 4 * o / 2)))) / (2*r))
    d_c_b_na = min(1, (o + r/2 * b_na + r/2 * c_b_na+o/3) / (2*r))
    e_nd_c_b_na = min(1, (o + r/2 * b_na + r/2 * c_b_na + 2 * o / 3) / (2*r))
    f_ne_nd_c_b_na = min(1, (o + r/2 * b_na + r/2 * c_b_na + 3*o / 3) / (2*r))
    d_nc_b_na = min(1, (o + e_d_nc_b_na * (r/2 * b_na + r/2 * e_d_nc_b_na + 2 * o / 3)
                        + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (r/2 * b_na + r/2 * f_ne_d_nc_b_na + 3*o / 3)
                                               + (1 - f_ne_d_nc_b_na) * (r * b_na + 4 * o / 2))) / (2*r))
    e_d_nc_b_na = min(
        1, (o + r/2 * b_na + r/2 * d_nc_b_na + 2 * o / 3) / (2*r))
    f_ne_d_nc_b_na = min(
        1, (o + r/2 * b_na + r/2 * d_nc_b_na + 3*o / 3) / (2*r))
    e_nd_nc_b_na = min(1, (o + f_e_nd_nc_b_na * (r/2 * b_na + r/2 * f_e_nd_nc_b_na + 3*o / 3)
                           + (1 - f_e_nd_nc_b_na) * (r * b_na + 4 * o / 2)) / (2*r))
    f_e_nd_nc_b_na = min(
        1, (o + r/2 * b_na + r/2 * e_nd_nc_b_na + 3*o / 3) / (2*r))
    f_ne_nd_nc_b_na = min(1, (o+r*b_na+4 * o / 2)/(2*r))
    c_nb_na = min(1, (o + d_c_nb_na * (e_d_c_nb_na * (r/2 * d_c_nb_na + r/2 * e_d_c_nb_na + 2 * o / 3)
                                       + (1 - e_d_c_nb_na) * (f_ne_d_c_nb_na * (r/2 * d_c_nb_na + r/2 * f_ne_d_c_nb_na + 3*o / 3)
                                                              + (1 - f_ne_d_c_nb_na) * (r * d_c_nb_na + 4 * o / 2)))
                      + (1 - d_c_nb_na) * (e_nd_c_nb_na * (f_e_nd_c_nb_na * (r/2 * e_nd_c_nb_na + r/2 * f_e_nd_c_nb_na + 3*o / 3)
                                                           + (1 - f_e_nd_c_nb_na) * (r * e_nd_c_nb_na + 4 * o / 2))
                                           + (1 - e_nd_c_nb_na) * (f_ne_nd_c_nb_na * (r * f_ne_nd_c_nb_na + 4 * o / 2)
                                                                   + (1 - f_ne_nd_c_nb_na) * 5*o))) / ((2*r) * (1 - (1 - d_c_nb_na) * (1 - e_nd_c_nb_na) * (1-f_ne_nd_c_nb_na))))
    d_c_nb_na = min(1, (o + e_d_c_nb_na * (r/2 * c_nb_na + r/2 * e_d_c_nb_na + 2 * o / 3)
                        + (1 - e_d_c_nb_na) * ((f_ne_d_c_nb_na) * (r/2 * c_nb_na + r/2 * f_ne_d_c_nb_na + 3*o / 3)
                                               + (1 - f_ne_d_c_nb_na) * (r * c_nb_na + 4 * o / 2))) / (2*r))
    e_d_c_nb_na = min(1, (o + r/2 * c_nb_na + r/2 *
                          d_c_nb_na + 2 * o / 3) / (2*r))
    f_ne_d_c_nb_na = min(
        1, (o + r/2 * c_nb_na + r/2 * d_c_nb_na + 3*o / 3) / (2*r))
    e_nd_c_nb_na = min(1, (o + f_e_nd_c_nb_na * (r/2 * c_nb_na + r/2 * f_e_nd_c_nb_na + 3*o / 3)
                           + (1 - f_e_nd_c_nb_na) * (r * c_nb_na + 4 * o / 2)) / (2*r))
    f_e_nd_c_nb_na = min(1, (o + r/2 * c_nb_na + r/2 *
                             e_nd_c_nb_na + 3*o / 3) / (2*r))
    f_ne_nd_c_nb_na = min(1, (o + r * c_nb_na + 4 * o / 2) / (2*r))
    d_nc_nb_na = min(1, (o + e_d_nc_nb_na * (f_e_d_nc_nb_na * (r/2 * e_d_nc_nb_na + r/2 * f_e_d_nc_nb_na + 3*o / 3)
                                             + (1 - f_e_d_nc_nb_na) * (r * e_d_nc_nb_na + 4 * o / 2))
                         + (1 - e_d_nc_nb_na) * (f_ne_d_nc_nb_na * (r * f_ne_d_nc_nb_na + 4 * o / 2)
                                                 + (1 - f_ne_d_nc_nb_na) * 5*o)) / ((2*r) * (e_d_nc_nb_na + (1 - e_d_nc_nb_na) * f_ne_d_nc_nb_na)))
    e_d_nc_nb_na = min(1, (o + f_e_d_nc_nb_na * (r/2 * d_nc_nb_na + r/2 * f_e_d_nc_nb_na + 3*o / 3)
                           + (1 - f_e_d_nc_nb_na) * (r * d_nc_nb_na + 4 * o / 2)) / (2*r))
    f_e_d_nc_nb_na = min(1, (o + r/2 * d_nc_nb_na + r/2 *
                             e_d_nc_nb_na + 3*o / 3) / (2*r))
    f_ne_d_nc_nb_na = min(1, (o + r * d_nc_nb_na + 4 * o / 2) / (2*r))
    e_nd_nc_nb_na = min(1, (o + f_e_nd_nc_nb_na * (r * f_e_nd_nc_nb_na + 4 * o / 2)
                            + (1 - f_e_nd_nc_nb_na) * 5*o) / ((2*r) * f_e_nd_nc_nb_na))
    f_e_nd_nc_nb_na = min(1, (o+r*e_nd_nc_nb_na+4 * o / 2)/(2*r))


print('a =', a)
print('b_a =', b_a)
print('c_b_a =', c_b_a)
print('d_nc_b_a =', d_nc_b_a)
print('e_nd_nc_b_a =', e_nd_nc_b_a)
print('f_ne_nd_nc_b_a =', f_ne_nd_nc_b_a)
print('c_nb_a =', c_nb_a)
print('d_c_nb_a =', d_c_nb_a)
print('e_nd_c_nb_a =', e_nd_c_nb_a)
print('f_ne_nd_c_nb_a =', f_ne_nd_c_nb_a)
print('d_nc_nb_a =', d_nc_nb_a)
print('e_d_nc_nb_a =', e_d_nc_nb_a)
print('f_ne_d_nc_nb_a =', f_ne_d_nc_nb_a)
print('e_nd_nc_nb_a =', e_nd_nc_nb_a)
print('f_e_nd_nc_nb_a =', f_e_nd_nc_nb_a)
print('f_ne_nd_nc_nb_a =', f_ne_nd_nc_nb_a)
print('b_na =', b_na)
print('c_b_na =', c_b_na)
print('d_c_b_na =', d_c_b_na)
print('e_nd_c_b_na =', e_nd_c_b_na)
print('f_ne_nd_c_b_na =', f_ne_nd_c_b_na)
print('d_nc_b_na =', d_nc_b_na)
print('e_d_nc_b_na =', e_d_nc_b_na)
print('f_ne_d_nc_b_na =', f_ne_d_nc_b_na)
print('e_nd_nc_b_na =', e_nd_nc_b_na)
print('f_e_nd_nc_b_na =', f_e_nd_nc_b_na)
print('f_ne_nd_nc_b_na =', f_ne_nd_nc_b_na)
print('c_nb_na =', c_nb_na)
print('d_c_nb_na =', d_c_nb_na)
print('e_d_c_nb_na =', e_d_c_nb_na)
print('f_ne_d_c_nb_na =', f_ne_d_c_nb_na)
print('e_nd_c_nb_na =', e_nd_c_nb_na)
print('f_e_nd_c_nb_na =', f_e_nd_c_nb_na)
print('f_ne_nd_c_nb_na =', f_ne_nd_c_nb_na)
print('d_nc_nb_na =', d_nc_nb_na)
print('e_d_nc_nb_na =', e_d_nc_nb_na)
print('f_e_d_nc_nb_na =', f_e_d_nc_nb_na)
print('f_ne_d_nc_nb_na =', f_ne_d_nc_nb_na)
print('e_nd_nc_nb_na =', e_nd_nc_nb_na)
print('f_e_nd_nc_nb_na =', f_e_nd_nc_nb_na)


ABC = a * b_a * c_b_a
ABD = a * b_a * (1 - c_b_a) * d_nc_b_a
ABE = a * b_a * (1 - c_b_a) * (1-d_nc_b_a) * e_nd_nc_b_a
ABF = a * b_a * (1 - c_b_a) * (1 - d_nc_b_a) * \
    (1 - e_nd_nc_b_a) * f_ne_nd_nc_b_a
AB = a * b_a * (1 - c_b_a) * (1 - d_nc_b_a) * \
    (1 - e_nd_nc_b_a) * (1-f_ne_nd_nc_b_a)
ACD = a * (1 - b_a) * c_nb_a * d_c_nb_a
ACE = a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * e_nd_c_nb_a
ACF = a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * (1-e_nd_c_nb_a) * f_ne_nd_c_nb_a
AC = a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * \
    (1-e_nd_c_nb_a) * (1-f_ne_nd_c_nb_a)
ADE = a * (1 - b_a) * (1 - c_nb_a) * d_nc_nb_a * e_d_nc_nb_a
ADF = a * (1 - b_a) * (1 - c_nb_a) * d_nc_nb_a * \
    (1-e_d_nc_nb_a) * f_ne_d_nc_nb_a
AD = a * (1 - b_a) * (1 - c_nb_a) * d_nc_nb_a * \
    (1-e_d_nc_nb_a) * (1-f_ne_d_nc_nb_a)
AEF = a * (1 - b_a) * (1 - c_nb_a) * (1-d_nc_nb_a) * \
    e_nd_nc_nb_a * f_e_nd_nc_nb_a
AE = a * (1 - b_a) * (1 - c_nb_a) * (1-d_nc_nb_a) * \
    e_nd_nc_nb_a * (1-f_e_nd_nc_nb_a)
AF = a * (1 - b_a) * (1 - c_nb_a) * (1 - d_nc_nb_a) * \
    (1 - e_nd_nc_nb_a) * f_ne_nd_nc_nb_a
A = a * (1 - b_a) * (1 - c_nb_a) * (1-d_nc_nb_a) * \
    (1-e_nd_nc_nb_a) * (1-f_ne_nd_nc_nb_a)
BCD = (1 - a) * (b_na) * c_b_na * d_c_b_na
BCE = (1 - a) * (b_na) * c_b_na * (1-d_c_b_na) * e_nd_c_b_na
BCF = (1 - a) * (b_na) * c_b_na * (1-d_c_b_na) * \
    (1-e_nd_c_b_na) * f_ne_nd_c_b_na
BC = (1 - a) * (b_na) * c_b_na * (1-d_c_b_na) * \
    (1-e_nd_c_b_na) * (1-f_ne_nd_c_b_na)
BDE = (1 - a) * (b_na) * (1 - c_b_na) * d_nc_b_na * e_d_nc_b_na
BDF = (1 - a) * (b_na) * (1 - c_b_na) * \
    d_nc_b_na * (1-e_d_nc_b_na) * f_ne_d_nc_b_na
BD = (1 - a) * (b_na) * (1 - c_b_na) * d_nc_b_na * \
    (1-e_d_nc_b_na) * (1-f_ne_d_nc_b_na)
BEF = (1 - a) * (b_na) * (1 - c_b_na) * \
    (1 - d_nc_b_na) * e_nd_nc_b_na * f_e_nd_nc_b_na
BE = (1 - a) * (b_na) * (1 - c_b_na) * \
    (1-d_nc_b_na) * e_nd_nc_b_na * (1-f_e_nd_nc_b_na)
BF = (1 - a) * (b_na) * (1 - c_b_na) * (1-d_nc_b_na) * \
    (1-e_nd_nc_b_na) * f_ne_nd_nc_b_na
B = (1 - a) * (b_na) * (1 - c_b_na) * (1-d_nc_b_na) * \
    (1-e_nd_nc_b_na) * (1-f_e_nd_nc_b_na)
CDE = (1 - a) * (1 - b_na) * c_nb_na * d_c_nb_na * e_d_c_nb_na
CDF = (1 - a) * (1 - b_na) * c_nb_na * \
    d_c_nb_na * (1-e_d_c_nb_na) * f_ne_d_c_nb_na
CD = (1 - a) * (1 - b_na) * c_nb_na * d_c_nb_na * \
    (1-e_d_c_nb_na) * (1-f_ne_d_c_nb_na)
CEF = (1 - a) * (1 - b_na) * c_nb_na * \
    (1-d_c_nb_na) * e_nd_c_nb_na * f_e_nd_c_nb_na
CE = (1 - a) * (1 - b_na) * c_nb_na * (1-d_c_nb_na) * \
    e_nd_c_nb_na * (1-f_e_nd_c_nb_na)
CF = (1 - a) * (1 - b_na) * c_nb_na * (1-d_c_nb_na) * \
    (1-e_nd_c_nb_na) * f_ne_nd_c_nb_na
C = (1 - a) * (1 - b_na) * c_nb_na * (1-d_c_nb_na) * \
    (1-e_nd_c_nb_na) * (1-f_ne_nd_c_nb_na)
DEF = (1 - a) * (1 - b_na) * (1-c_nb_na) * \
    d_nc_nb_na * e_d_nc_nb_na * f_e_d_nc_nb_na
DE = (1 - a) * (1 - b_na) * (1-c_nb_na) * \
    d_nc_nb_na * e_d_nc_nb_na * (1-f_e_d_nc_nb_na)
DF = (1 - a) * (1 - b_na) * (1 - c_nb_na) * \
    d_nc_nb_na * (1 - e_d_nc_nb_na) * f_ne_d_nc_nb_na
D = (1 - a) * (1 - b_na) * (1 - c_nb_na) * d_nc_nb_na * \
    (1 - e_d_nc_nb_na) * (1-f_ne_d_nc_nb_na)
EF = (1 - a) * (1 - b_na) * (1-c_nb_na) * \
    (1-d_nc_nb_na) * e_nd_nc_nb_na * f_e_nd_nc_nb_na
E = (1 - a) * (1 - b_na) * (1-c_nb_na) * \
    (1-d_nc_nb_na) * e_nd_nc_nb_na * (1-f_e_nd_nc_nb_na)
F = (1 - a) * (1 - b_na) * (1-c_nb_na) * (1-d_nc_nb_na) * (1-e_nd_nc_nb_na)
print("ABC=", ABC)
print("ABD=", ABD)
print("ABE=", ABE)
print("ABF=", ABF)
print("AB =", AB)
print("ACD=", ACD)
print("ACE=", ACE)
print("ACF=", ACF)
print("AC =", AC)
print("ADE=", ADE)
print("ADF=", ADF)
print("AD =", AD)
print("AEF=", AEF)
print("AE =", AE)
print("AF =", AF)
print("A  =", A)
print("BCD=", BCD)
print("BCE=", BCE)
print("BCF=", BCF)
print("BC =", BC)
print("BDE=", BDE)
print("BDF=", BDF)
print("BD =", BD)
print("BEF=", BEF)
print("BE =", BE)
print("BF =", BF)
print("B  =", B)
print("CDE=", CDE)
print("CDF=", CDF)
print("CD =", CD)
print("CEF=", CEF)
print("CE =", CE)
print("CF =", CF)
print("C  =", C)
print("DEF=", DEF)
print("DE =", DE)
print("DF =", DF)
print("D  =", D)
print("EF =", EF)
print("E  =", E)
print("F  =", F)

hitori = A + B + C + D + E + F
sashi = AB + AC + AD + AE + AF + BC + BD + BE + BF + CD + CE + CF + DE + DF + EF
print("一人勝ち:", hitori)
print("サシ勝負:", sashi)
print("三人勝負:", 1 - hitori - sashi)
print("D追い込まれ:", ABC)
print("E追い込まれ:", ABC + ABD + ACD + BCD)
print("F追い込まれ:", ABC + ABD + ACD + BCD + ABE + ACE + ADE + BCE + BDE + CDE)

eva = -o * (1 - a)\
    + a*(b_a * (c_b_a * (r/2 * b_a + r/2 * c_b_a)
                + (1 - c_b_a) * (d_nc_b_a * (r/2 * b_a + r/2 * d_nc_b_a + o / 3)
                                 + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * b_a + r/2 * e_nd_nc_b_a + 2 * o / 3)
                                                     + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (r/2 * b_a + r/2 * f_ne_nd_nc_b_a + o)
                                                                            + (1 - f_ne_nd_nc_b_a) * (r * b_a + 4 * o / 2)))))
         + (1-b_a)*(c_nb_a * (d_c_nb_a * (r/2 * c_nb_a + r/2 * d_c_nb_a + o/3)
                              + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * c_nb_a + r/2 * e_nd_c_nb_a + 2 * o / 3)
                                                  + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (r/2 * c_nb_a + r/2 * f_ne_nd_c_nb_a + 3*o / 3)
                                                                         + (1 - f_ne_nd_c_nb_a) * (r * c_nb_a + 4 * o / 2))))
                    + (1 - c_nb_a) * (d_nc_nb_a * (e_d_nc_nb_a * (r/2 * d_nc_nb_a + r/2 * e_d_nc_nb_a + 2 * o / 3)
                                                   + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (r/2 * d_nc_nb_a + r/2 * f_ne_d_nc_nb_a + 3*o / 3)
                                                                          + (1 - f_ne_d_nc_nb_a) * (r * d_nc_nb_a + 4 * o / 2)))
                                      + (1 - d_nc_nb_a) * ((e_nd_nc_nb_a) * (f_e_nd_nc_nb_a *
                                                                             (r/2 * e_nd_nc_nb_a + r/2 *
                                                                              f_e_nd_nc_nb_a + 3*o / 3)
                                                                             + (1 - f_e_nd_nc_nb_a) * (r * e_nd_nc_nb_a + 4 * o / 2))
                                                           + (1 - e_nd_nc_nb_a) * (f_ne_nd_nc_nb_a * (r * f_ne_nd_nc_nb_a + 4 * o / 2)
                                                                                   + (1 - f_ne_nd_nc_nb_a) * 5*o)))))\
    - r*a*a*(1 - (1 - b_a) * (1 - c_nb_a) * (1 - d_nc_nb_a)
             * (1 - e_nd_nc_nb_a) * (1 - f_ne_nd_nc_nb_a))
evb = a * (-o * (1 - b_a)
           + b_a * (c_b_a * (r/2 * a + r/2 * c_b_a)
                    + (1 - c_b_a) * (d_nc_b_a * (r/2 * a + r/2 * d_nc_b_a + o / 3)
                                     + (1 - d_nc_b_a) * (e_nd_nc_b_a * (r/2 * a + r/2 * e_nd_nc_b_a + 2 * o / 3)
                                                         + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (r/2 * a + r/2 * f_ne_nd_nc_b_a + 3*o / 3)
                                                                                + (1 - f_ne_nd_nc_b_a) * (r * a + 4 * o / 2)))))
           - r * b_a * b_a)\
    + (1 - a) * (-o * (1 - b_na)
                 + b_na * (c_b_na * (d_c_b_na * (r/2 * c_b_na + r/2 * d_c_b_na + o/3)
                                     + (1 - d_c_b_na) * (e_nd_c_b_na * (r/2 * c_b_na + r/2 * e_nd_c_b_na + 2 * o / 3)
                                                         + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (r/2 * c_b_na + r/2 * f_ne_nd_c_b_na + 3*o / 3)
                                                                                + (1 - f_ne_nd_c_b_na) * (r * c_b_na + 4 * o / 2))))
                           + (1 - c_b_na) * (d_nc_b_na * (e_d_nc_b_na * (r/2 * d_nc_b_na + r/2 * e_d_nc_b_na + 2 * o / 3)
                                                          + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (r/2 * d_nc_b_na + r/2 * f_ne_d_nc_b_na + 3*o / 3)
                                                                                 + (1 - f_ne_d_nc_b_na) * (r * d_nc_b_na + 4 * o / 2)))
                                             + (1 - d_nc_b_na) * ((e_nd_nc_b_na) * (f_e_nd_nc_b_na *
                                                                                    (r/2 * e_nd_nc_b_na + r/2 *
                                                                                     f_e_nd_nc_b_na + 3*o / 3)
                                                                                    + (1 - f_e_nd_nc_b_na) * (r * e_nd_nc_b_na + 4 * o / 2))
                                                                  + (1 - e_nd_nc_b_na) * (f_ne_nd_nc_b_na * (r * f_ne_nd_nc_b_na + 4 * o / 2)
                                                                                          + (1 - f_ne_nd_nc_b_na) * 5*o))))
                 - r * b_na * b_na * ((1 - (1 - c_b_na) * (1 - d_nc_b_na) * (1 - e_nd_nc_b_na) * (1 - f_ne_nd_nc_b_na))))
evc = a * b_a * (-o * (1 - c_b_a)
                 + c_b_a * (r/2 * a + r/2 * b_a)
                 - r * c_b_a * c_b_a)\
    + a * (1 - b_a) * (-o * (1 - c_nb_a)
                       + c_nb_a * (d_c_nb_a * (r/2 * a + r/2 * d_c_nb_a+o/3)
                                   + (1 - d_c_nb_a) * (e_nd_c_nb_a * (r/2 * a + r/2 * e_nd_c_nb_a + 2 * o / 3)
                                                       + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (r/2 * a + r/2 * f_ne_nd_c_nb_a + 3*o / 3)
                                                                              + (1 - f_ne_nd_c_nb_a) * (r * a + 4 * o / 2))))
                       - r * c_nb_a * c_nb_a)\
    + (1 - a) * b_na * (-o * (1 - c_b_na)
                        + c_b_na * (d_c_b_na * (r/2 * b_na + r/2 * d_c_b_na+o/3)
                                    + (1 - d_c_b_na) * (e_nd_c_b_na * (r/2 * b_na + r/2 * e_nd_c_b_na + 2 * o / 3)
                                                        + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (r/2 * b_na + r/2 * f_ne_nd_c_b_na + 3*o / 3)
                                                                               + (1 - f_ne_nd_c_b_na) * (r * b_na + 4 * o / 2))))
                        - r * c_b_na * c_b_na)\
    + (1 - a) * (1 - b_na) * (-o * (1 - c_nb_na)
                              + c_nb_na * (d_c_nb_na * (e_d_c_nb_na * (r/2 * d_c_nb_na + r/2 * e_d_c_nb_na + 2 * o / 3)
                                                        + (1 - e_d_c_nb_na) * (f_ne_d_c_nb_na * (r/2 * d_c_nb_na + r/2 * f_ne_d_c_nb_na + 3*o / 3)
                                                                               + (1 - f_ne_d_c_nb_na) * (r * d_c_nb_na + 4 * o / 2)))
                                           + (1 - d_c_nb_na) * (e_nd_c_nb_na * (f_e_nd_c_nb_na * (r/2 * e_nd_c_nb_na + r/2 * f_e_nd_c_nb_na + 3*o / 3)
                                                                                + (1 - f_e_nd_c_nb_na) * (r * e_nd_c_nb_na + 4 * o / 2))
                                                                + (1 - e_nd_c_nb_na) * (f_ne_nd_c_nb_na * (r * f_ne_nd_c_nb_na + 4 * o / 2)
                                                                                        + (1 - f_ne_nd_c_nb_na) * 5*o)))
                              - r * c_nb_na * c_nb_na * (1 - (1 - d_c_nb_na) * (1 - e_nd_c_nb_na) * (1 - f_ne_nd_c_nb_na)))
evd = a * b_a * c_b_a * 0\
    + a * b_a * (1 - c_b_a) * (-o * (1 - d_nc_b_a)
                               + d_nc_b_a * (r/2 * a + r/2 * b_a + o / 3)
                               - r * d_nc_b_a * d_nc_b_a)\
    + a * (1 - b_a) * c_nb_a * (-o * (1 - d_c_nb_a)
                                + d_c_nb_a *
                                (r/2 * a + r/2 *
                                 c_nb_a+o/3)
                                - r * d_c_nb_a * d_c_nb_a)\
    + a * (1 - b_a) * (1 - c_nb_a) * (-o * (1 - d_nc_nb_a)
                                      + d_nc_nb_a * (e_d_nc_nb_a * (r/2 * a + r/2 * e_d_nc_nb_a + 2 * o / 3)
                                                     + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (r/2 * a + r/2 * f_ne_d_nc_nb_a + 3*o / 3)
                                                                            + (1 - f_ne_d_nc_nb_a) * (r * a + 4 * o / 2)))
                                      - r * d_nc_nb_a * d_nc_nb_a)\
    + (1 - a) * b_na * c_b_na * (-o * (1 - d_c_b_na)
                                 + d_c_b_na *
                                 (r/2 * b_na + r/2 * c_b_na+o/3)
                                 - r * d_c_b_na * d_c_b_na)\
    + (1 - a) * b_na * (1 - c_b_na) * (-o * (1 - d_nc_b_na)
                                       + d_nc_b_na * (e_d_nc_b_na * (r/2 * b_na + r/2 * e_d_nc_b_na + 2 * o / 3)
                                                      + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (r/2 * b_na + r/2 * f_ne_d_nc_b_na + 3*o / 3)
                                                                             + (1 - f_ne_d_nc_b_na) * (r * b_na + 4 * o / 2)))
                                       - r * d_nc_b_na * d_nc_b_na)\
    + (1 - a) * (1 - b_na) * c_nb_na * (-o * (1 - d_c_nb_na)
                                        + d_c_nb_na * (e_d_c_nb_na * (r/2 * c_nb_na + r/2 * e_d_c_nb_na + 2 * o / 3)
                                                       + (1 - e_d_c_nb_na) * ((f_ne_d_c_nb_na) * (r/2 * c_nb_na + r/2 * f_ne_d_c_nb_na + 3*o / 3)
                                                                              + (1 - f_ne_d_c_nb_na) * (r * c_nb_na + 4 * o / 2)))
                                        - r * d_c_nb_na * d_c_nb_na)\
    + (1 - a) * (1 - b_na) * (1 - c_nb_na) * (-o * (1 - d_nc_nb_na)
                                              + d_nc_nb_na * (e_d_nc_nb_na * (f_e_d_nc_nb_na * (r/2 * e_d_nc_nb_na + r/2 * f_e_d_nc_nb_na + 3*o / 3)
                                                                              + (1 - f_e_d_nc_nb_na) * (r * e_d_nc_nb_na + 4 * o / 2))
                                                              + (1 - e_d_nc_nb_na) * (f_ne_d_nc_nb_na * (r * f_ne_d_nc_nb_na + 4 * o / 2)
                                                                                      + (1 - f_ne_d_nc_nb_na) * 5*o))
                                              - r*d_nc_nb_na*d_nc_nb_na*(e_d_nc_nb_na + (1 - e_d_nc_nb_na) * f_ne_d_nc_nb_na))
eve = a * b_a * c_b_a * 0\
    + a * b_a * (1 - c_b_a) * d_nc_b_a * 0\
    + a * b_a * (1 - c_b_a) * (1-d_nc_b_a) * (-o*(1-e_nd_nc_b_a) +
                                              e_nd_nc_b_a * (r/2 * a + r/2 * b_a + 2 * o / 3) - r * e_nd_nc_b_a * e_nd_nc_b_a)\
    + a * (1 - b_a) * c_nb_a * d_c_nb_a * 0\
    + a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * \
    (-o * (1 - e_nd_c_nb_a) + e_nd_c_nb_a * (r/2 * a + r/2 * c_nb_a + 2 * o / 3) - r * e_nd_c_nb_a * e_nd_c_nb_a)\
    + a * (1 - b_a) * (1-c_nb_a) * d_nc_nb_a * \
    (-o * (1 - e_d_nc_nb_a) + e_d_nc_nb_a * (r/2 * a + r/2 * d_nc_nb_a + 2 * o / 3) - r * e_d_nc_nb_a * e_d_nc_nb_a)\
    + a * (1 - b_a) * (1-c_nb_a) * (1-d_nc_nb_a) * (-o*(1-e_nd_nc_nb_a)+e_nd_nc_nb_a*(f_e_nd_nc_nb_a * (r/2 * a + r/2 * f_e_nd_nc_nb_a + 3*o / 3)
                                                                                      + (1 - f_e_nd_nc_nb_a) * (r * a + 4 * o / 2)) - r * e_nd_nc_nb_a * e_nd_nc_nb_a)\
    + (1 - a) * b_na * c_b_na * d_c_b_na * 0\
    + (1 - a) * b_na * c_b_na * (1-d_c_b_na) * \
    (-o * (1 - e_nd_c_b_na) + e_nd_c_b_na * (r/2 * b_na + r/2 * c_b_na + 2 * o / 3) - r * e_nd_c_b_na * e_nd_c_b_na)\
    + (1 - a) * b_na * (1-c_b_na) * d_nc_b_na * \
    (-o * (1 - e_d_nc_b_na) + e_d_nc_b_na * (r/2 * b_na + r/2 * d_nc_b_na + 2 * o / 3) - r * e_d_nc_b_na * e_d_nc_b_na)\
    + (1 - a) * b_na * (1 - c_b_na) * (1 - d_nc_b_na) * (-o * (1 - e_nd_nc_b_na)+e_nd_nc_b_na*(f_e_nd_nc_b_na * (r/2 * b_na + r/2 * f_e_nd_nc_b_na + 3*o / 3)
                                                                                               + (1 - f_e_nd_nc_b_na) * (r * b_na + 4 * o / 2)) - r * e_nd_nc_b_na * e_nd_nc_b_na)\
    + (1 - a) * (1-b_na) * c_nb_na * d_c_nb_na * \
    (-o * (1 - e_d_c_nb_na) + e_d_c_nb_na * (r/2 * c_nb_na + r/2 * d_c_nb_na + 2 * o / 3) - r * e_d_c_nb_na * e_d_c_nb_na)\
    + (1 - a) * (1-b_na) * c_nb_na * (1-d_c_nb_na) * (-o*(1-e_nd_c_nb_na)+e_nd_c_nb_na*(f_e_nd_c_nb_na * (r/2 * c_nb_na + r/2 * f_e_nd_c_nb_na + 3*o / 3)
                                                                                        + (1 - f_e_nd_c_nb_na) * (r * c_nb_na + 4 * o / 2)) - r * e_nd_c_nb_na * e_nd_c_nb_na)\
    + (1 - a) * (1-b_na) * (1-c_nb_na) * d_nc_nb_na * (-o*(1-e_d_nc_nb_na)+e_d_nc_nb_na*(f_e_d_nc_nb_na * (r/2 * d_nc_nb_na + r/2 * f_e_d_nc_nb_na + 3*o / 3)
                                                                                         + (1 - f_e_d_nc_nb_na) * (r * d_nc_nb_na + 4 * o / 2)) - r * e_d_nc_nb_na * e_d_nc_nb_na)\
    + (1 - a) * (1-b_na) * (1-c_nb_na) * (1-d_nc_nb_na) * (-o*(1-e_nd_nc_nb_na)+e_nd_nc_nb_na*(f_e_nd_nc_nb_na * (r * f_e_nd_nc_nb_na + 4 * o / 2)
                                                                                               + (1 - f_e_nd_nc_nb_na) * 5*o)-r*e_nd_nc_nb_na*e_nd_nc_nb_na*(f_e_nd_nc_nb_na))
evf = -eva - evb - evc - evd - eve
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
print("evd=", evd)
print("eve=", eve)
print("evf=", evf)
