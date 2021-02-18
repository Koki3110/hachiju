import matplotlib.pyplot as plt
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
    a = (20
         + b_a * (c_b_a * (40 * b_a + 40 * c_b_a)
                  + (1 - c_b_a) * (d_nc_b_a * (40 * b_a + 40 * d_nc_b_a + 20 / 3)
                                   + (1 - d_nc_b_a) * (e_nd_nc_b_a * (40 * b_a + 40 * e_nd_nc_b_a + 40 / 3)
                                                       + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (40 * b_a + 40 * f_ne_nd_nc_b_a + 20)
                                                                              + (1 - f_ne_nd_nc_b_a) * (80 * b_a + 40)))))
         + (1-b_a)*(c_nb_a * (d_c_nb_a * (40 * c_nb_a + 40 * d_c_nb_a + 20/3)
                              + (1 - d_c_nb_a) * (e_nd_c_nb_a * (40 * c_nb_a + 40 * e_nd_c_nb_a + 40 / 3)
                                                  + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (40 * c_nb_a + 40 * f_ne_nd_c_nb_a + 60 / 3)
                                                                         + (1 - f_ne_nd_c_nb_a) * (80 * c_nb_a + 40))))
                    + (1 - c_nb_a) * (d_nc_nb_a * (e_d_nc_nb_a * (40 * d_nc_nb_a + 40 * e_d_nc_nb_a + 40 / 3)
                                                   + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (40 * d_nc_nb_a + 40 * f_ne_d_nc_nb_a + 60 / 3)
                                                                          + (1 - f_ne_d_nc_nb_a) * (80 * d_nc_nb_a + 40)))
                                      + (1 - d_nc_nb_a) * ((e_nd_nc_nb_a) * (f_e_nd_nc_nb_a *
                                                                             (40 * e_nd_nc_nb_a + 40 *
                                                                              f_e_nd_nc_nb_a + 60 / 3)
                                                                             + (1 - f_e_nd_nc_nb_a) * (80 * e_nd_nc_nb_a + 40))
                                                           + (1 - e_nd_nc_nb_a) * (f_ne_nd_nc_nb_a * (80 * f_ne_nd_nc_nb_a + 40)
                                                                                   + (1 - f_ne_nd_nc_nb_a) * 100)))))\
        / (160 * (1 - (1 - b_a) * (1 - c_nb_a) * (1 - d_nc_nb_a) * (1 - e_nd_nc_nb_a) * (1 - f_ne_nd_nc_nb_a)))
    b_a = (20
           + c_b_a * (40 * a + 40 * c_b_a)
           + (1 - c_b_a) * (d_nc_b_a * (40 * a + 40 * d_nc_b_a + 20 / 3)
                            + (1 - d_nc_b_a) * (e_nd_nc_b_a * (40 * a + 40 * e_nd_nc_b_a + 40 / 3)
                                                + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (40 * a + 40 * f_ne_nd_nc_b_a + 60 / 3)
                                                                       + (1 - f_ne_nd_nc_b_a) * (80 * a + 40))))) / 160
    c_b_a = (20 + 40 * a + 40 * b_a) / 160
    d_nc_b_a = (20 + 40 * a + 40 * b_a + 20/3) / 160
    e_nd_nc_b_a = (20+40*a+40*b_a+40/3)/160
    f_ne_nd_nc_b_a = (20 + 40 * a + 40 * b_a + 60 / 3) / 160
    #
    c_nb_a = (20 + d_c_nb_a * (40 * a + 40 * d_c_nb_a+20/3)
              + (1 - d_c_nb_a) * (e_nd_c_nb_a * (40 * a + 40 * e_nd_c_nb_a + 40 / 3)
                                  + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (40 * a + 40 * f_ne_nd_c_nb_a + 60 / 3)
                                                         + (1 - f_ne_nd_c_nb_a) * (80 * a + 40)))) / 160
    d_c_nb_a = (20 + 40 * a + 40 * c_nb_a+20/3) / 160
    e_nd_c_nb_a = (20 + 40 * a + 40 * c_nb_a + 40 / 3) / 160
    f_ne_nd_c_nb_a = (20 + 40 * a + 40 * c_nb_a + 60 / 3) / 160
    d_nc_nb_a = (20 + e_d_nc_nb_a * (40 * a + 40 * e_d_nc_nb_a + 40 / 3)
                 + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (40 * a + 40 * f_ne_d_nc_nb_a + 60 / 3)
                                        + (1 - f_ne_d_nc_nb_a) * (80 * a + 40))) / 160
    e_d_nc_nb_a = (20 + 40 * a + 40 * d_nc_nb_a + 40 / 3) / 160
    f_ne_d_nc_nb_a = (20 + 40 * a + 40 * d_nc_nb_a + 60 / 3) / 160
    e_nd_nc_nb_a = (20 + f_e_nd_nc_nb_a * (40 * a + 40 * f_e_nd_nc_nb_a + 60 / 3)
                    + (1 - f_e_nd_nc_nb_a) * (80 * a + 40)) / 160
    f_e_nd_nc_nb_a = (20 + 40 * a + 40 * e_nd_nc_nb_a + 60 / 3) / 160
    f_ne_nd_nc_nb_a = (20 + 80 * a + 40) / 160
    #
    b_na = (20 + c_b_na * (d_c_b_na * (40 * c_b_na + 40 * d_c_b_na + 20/3)
                           + (1 - d_c_b_na) * (e_nd_c_b_na * (40 * c_b_na + 40 * e_nd_c_b_na + 40 / 3)
                                               + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (40 * c_b_na + 40 * f_ne_nd_c_b_na + 60 / 3)
                                                                      + (1 - f_ne_nd_c_b_na) * (80 * c_b_na + 40))))
            + (1 - c_b_na) * (d_nc_b_na * (e_d_nc_b_na * (40 * d_nc_b_na + 40 * e_d_nc_b_na + 40 / 3)
                                           + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (40 * d_nc_b_na + 40 * f_ne_d_nc_b_na + 60 / 3)
                                                                  + (1 - f_ne_d_nc_b_na) * (80 * d_nc_b_na + 40)))
                              + (1 - d_nc_b_na) * ((e_nd_nc_b_na) * (f_e_nd_nc_b_na *
                                                                     (40 * e_nd_nc_b_na + 40 *
                                                                      f_e_nd_nc_b_na + 60 / 3)
                                                                     + (1 - f_e_nd_nc_b_na) * (80 * e_nd_nc_b_na + 40))
                                                   + (1 - e_nd_nc_b_na) * (f_ne_nd_nc_b_na * (80 * f_ne_nd_nc_b_na + 40)
                                                                           + (1 - f_ne_nd_nc_b_na) * 100))))\
        / (160 * (1 - (1 - c_b_na) * (1 - d_nc_b_na) * (1 - e_nd_nc_b_na) * (1 - f_ne_nd_nc_b_na)))
    c_b_na = (20 + d_c_b_na * (40 * b_na + 40 * d_c_b_na+20/3)
              + (1 - d_c_b_na) * (e_nd_c_b_na * (40 * b_na + 40 * e_nd_c_b_na + 40 / 3)
                                  + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (40 * b_na + 40 * f_ne_nd_c_b_na + 60 / 3)
                                                         + (1 - f_ne_nd_c_b_na) * (80 * b_na + 40)))) / 160
    d_c_b_na = (20 + 40 * b_na + 40 * c_b_na+20/3) / 160
    e_nd_c_b_na = (20 + 40 * b_na + 40 * c_b_na + 40 / 3) / 160
    f_ne_nd_c_b_na = (20 + 40 * b_na + 40 * c_b_na + 60 / 3) / 160
    d_nc_b_na = (20 + e_d_nc_b_na * (40 * b_na + 40 * e_d_nc_b_na + 40 / 3)
                 + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (40 * b_na + 40 * f_ne_d_nc_b_na + 60 / 3)
                                        + (1 - f_ne_d_nc_b_na) * (80 * b_na + 40))) / 160
    e_d_nc_b_na = (20 + 40 * b_na + 40 * d_nc_b_na + 40 / 3) / 160
    f_ne_d_nc_b_na = (20 + 40 * b_na + 40 * d_nc_b_na + 60 / 3) / 160
    e_nd_nc_b_na = (20 + f_e_nd_nc_b_na * (40 * b_na + 40 * f_e_nd_nc_b_na + 60 / 3)
                    + (1 - f_e_nd_nc_b_na) * (80 * b_na + 40)) / 160
    f_e_nd_nc_b_na = (20 + 40 * b_na + 40 * e_nd_nc_b_na + 60 / 3) / 160
    f_ne_nd_nc_b_na = (20+80*b_na+40)/160
    c_nb_na = (20 + d_c_nb_na * (e_d_c_nb_na * (40 * d_c_nb_na + 40 * e_d_c_nb_na + 40 / 3)
                                 + (1 - e_d_c_nb_na) * (f_ne_d_c_nb_na * (40 * d_c_nb_na + 40 * f_ne_d_c_nb_na + 60 / 3)
                                                        + (1 - f_ne_d_c_nb_na) * (80 * d_c_nb_na + 40)))
               + (1 - d_c_nb_na) * (e_nd_c_nb_na * (f_e_nd_c_nb_na * (40 * e_nd_c_nb_na + 40 * f_e_nd_c_nb_na + 60 / 3)
                                                    + (1 - f_e_nd_c_nb_na) * (80 * e_nd_c_nb_na + 40))
                                    + (1 - e_nd_c_nb_na) * (f_ne_nd_c_nb_na * (80 * f_ne_nd_c_nb_na + 40)
                                                            + (1 - f_ne_nd_c_nb_na) * 100))) / (160 * (1 - (1 - d_c_nb_na) * (1 - e_nd_c_nb_na) * (1-f_ne_nd_c_nb_na)))
    d_c_nb_na = (20 + e_d_c_nb_na * (40 * c_nb_na + 40 * e_d_c_nb_na + 40 / 3)
                 + (1 - e_d_c_nb_na) * ((f_ne_d_c_nb_na) * (40 * c_nb_na + 40 * f_ne_d_c_nb_na + 60 / 3)
                                        + (1 - f_ne_d_c_nb_na) * (80 * c_nb_na + 40))) / 160
    e_d_c_nb_na = (20 + 40 * c_nb_na + 40 * d_c_nb_na + 40/3) / 160
    f_ne_d_c_nb_na = (20 + 40 * c_nb_na + 40 * d_c_nb_na + 60 / 3) / 160
    e_nd_c_nb_na = (20 + f_e_nd_c_nb_na * (40 * c_nb_na + 40 * f_e_nd_c_nb_na + 60 / 3)
                    + (1 - f_e_nd_c_nb_na) * (80 * c_nb_na + 40)) / 160
    f_e_nd_c_nb_na = (20 + 40 * c_nb_na + 40 * e_nd_c_nb_na + 60 / 3) / 160
    f_ne_nd_c_nb_na = (20 + 80 * c_nb_na + 40) / 160
    d_nc_nb_na = (20 + e_d_nc_nb_na * (f_e_d_nc_nb_na * (40 * e_d_nc_nb_na + 40 * f_e_d_nc_nb_na + 60 / 3)
                                       + (1 - f_e_d_nc_nb_na) * (80 * e_d_nc_nb_na + 40))
                  + (1 - e_d_nc_nb_na) * (f_ne_d_nc_nb_na * (80 * f_ne_d_nc_nb_na + 40)
                                          + (1 - f_ne_d_nc_nb_na) * 100)) / (160 * (e_d_nc_nb_na + (1 - e_d_nc_nb_na) * f_ne_d_nc_nb_na))
    e_d_nc_nb_na = (20 + f_e_d_nc_nb_na * (40 * d_nc_nb_na + 40 * f_e_d_nc_nb_na + 60 / 3)
                    + (1 - f_e_d_nc_nb_na) * (80 * d_nc_nb_na + 40)) / 160
    f_e_d_nc_nb_na = (20 + 40 * d_nc_nb_na + 40 * e_d_nc_nb_na + 60 / 3) / 160
    f_ne_d_nc_nb_na = (20 + 80 * d_nc_nb_na + 40) / 160
    e_nd_nc_nb_na = (20 + f_e_nd_nc_nb_na * (80 * f_e_nd_nc_nb_na + 40)
                     + (1 - f_e_nd_nc_nb_na) * 100) / (160 * f_e_nd_nc_nb_na)
    f_e_nd_nc_nb_na = (20+80*e_nd_nc_nb_na+40)/160


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

eva = -20 * (1 - a)\
    + a*(b_a * (c_b_a * (40 * b_a + 40 * c_b_a)
                + (1 - c_b_a) * (d_nc_b_a * (40 * b_a + 40 * d_nc_b_a + 20 / 3)
                                 + (1 - d_nc_b_a) * (e_nd_nc_b_a * (40 * b_a + 40 * e_nd_nc_b_a + 40 / 3)
                                                     + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (40 * b_a + 40 * f_ne_nd_nc_b_a + 20)
                                                                            + (1 - f_ne_nd_nc_b_a) * (80 * b_a + 40)))))
         + (1-b_a)*(c_nb_a * (d_c_nb_a * (40 * c_nb_a + 40 * d_c_nb_a + 20/3)
                              + (1 - d_c_nb_a) * (e_nd_c_nb_a * (40 * c_nb_a + 40 * e_nd_c_nb_a + 40 / 3)
                                                  + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (40 * c_nb_a + 40 * f_ne_nd_c_nb_a + 60 / 3)
                                                                         + (1 - f_ne_nd_c_nb_a) * (80 * c_nb_a + 40))))
                    + (1 - c_nb_a) * (d_nc_nb_a * (e_d_nc_nb_a * (40 * d_nc_nb_a + 40 * e_d_nc_nb_a + 40 / 3)
                                                   + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (40 * d_nc_nb_a + 40 * f_ne_d_nc_nb_a + 60 / 3)
                                                                          + (1 - f_ne_d_nc_nb_a) * (80 * d_nc_nb_a + 40)))
                                      + (1 - d_nc_nb_a) * ((e_nd_nc_nb_a) * (f_e_nd_nc_nb_a *
                                                                             (40 * e_nd_nc_nb_a + 40 *
                                                                              f_e_nd_nc_nb_a + 60 / 3)
                                                                             + (1 - f_e_nd_nc_nb_a) * (80 * e_nd_nc_nb_a + 40))
                                                           + (1 - e_nd_nc_nb_a) * (f_ne_nd_nc_nb_a * (80 * f_ne_nd_nc_nb_a + 40)
                                                                                   + (1 - f_ne_nd_nc_nb_a) * 100)))))\
    - 80*a*a*(1 - (1 - b_a) * (1 - c_nb_a) * (1 - d_nc_nb_a)
              * (1 - e_nd_nc_nb_a) * (1 - f_ne_nd_nc_nb_a))
evb = a * (-20 * (1 - b_a)
           + b_a * (c_b_a * (40 * a + 40 * c_b_a)
                    + (1 - c_b_a) * (d_nc_b_a * (40 * a + 40 * d_nc_b_a + 20 / 3)
                                     + (1 - d_nc_b_a) * (e_nd_nc_b_a * (40 * a + 40 * e_nd_nc_b_a + 40 / 3)
                                                         + (1 - e_nd_nc_b_a) * (f_ne_nd_nc_b_a * (40 * a + 40 * f_ne_nd_nc_b_a + 60 / 3)
                                                                                + (1 - f_ne_nd_nc_b_a) * (80 * a + 40)))))
           - 80 * b_a * b_a)\
    + (1 - a) * (-20 * (1 - b_na)
                 + b_na * (c_b_na * (d_c_b_na * (40 * c_b_na + 40 * d_c_b_na + 20/3)
                                     + (1 - d_c_b_na) * (e_nd_c_b_na * (40 * c_b_na + 40 * e_nd_c_b_na + 40 / 3)
                                                         + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (40 * c_b_na + 40 * f_ne_nd_c_b_na + 60 / 3)
                                                                                + (1 - f_ne_nd_c_b_na) * (80 * c_b_na + 40))))
                           + (1 - c_b_na) * (d_nc_b_na * (e_d_nc_b_na * (40 * d_nc_b_na + 40 * e_d_nc_b_na + 40 / 3)
                                                          + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (40 * d_nc_b_na + 40 * f_ne_d_nc_b_na + 60 / 3)
                                                                                 + (1 - f_ne_d_nc_b_na) * (80 * d_nc_b_na + 40)))
                                             + (1 - d_nc_b_na) * ((e_nd_nc_b_na) * (f_e_nd_nc_b_na *
                                                                                    (40 * e_nd_nc_b_na + 40 *
                                                                                     f_e_nd_nc_b_na + 60 / 3)
                                                                                    + (1 - f_e_nd_nc_b_na) * (80 * e_nd_nc_b_na + 40))
                                                                  + (1 - e_nd_nc_b_na) * (f_ne_nd_nc_b_na * (80 * f_ne_nd_nc_b_na + 40)
                                                                                          + (1 - f_ne_nd_nc_b_na) * 100))))
                 - 80 * b_na * b_na * ((1 - (1 - c_b_na) * (1 - d_nc_b_na) * (1 - e_nd_nc_b_na) * (1 - f_ne_nd_nc_b_na))))
evc = a * b_a * (-20 * (1 - c_b_a)
                 + c_b_a * (40 * a + 40 * b_a)
                 - 80 * c_b_a * c_b_a)\
    + a * (1 - b_a) * (-20 * (1 - c_nb_a)
                       + c_nb_a * (d_c_nb_a * (40 * a + 40 * d_c_nb_a+20/3)
                                   + (1 - d_c_nb_a) * (e_nd_c_nb_a * (40 * a + 40 * e_nd_c_nb_a + 40 / 3)
                                                       + (1 - e_nd_c_nb_a) * (f_ne_nd_c_nb_a * (40 * a + 40 * f_ne_nd_c_nb_a + 60 / 3)
                                                                              + (1 - f_ne_nd_c_nb_a) * (80 * a + 40))))
                       - 80 * c_nb_a * c_nb_a)\
    + (1 - a) * b_na * (-20 * (1 - c_b_na)
                        + c_b_na * (d_c_b_na * (40 * b_na + 40 * d_c_b_na+20/3)
                                    + (1 - d_c_b_na) * (e_nd_c_b_na * (40 * b_na + 40 * e_nd_c_b_na + 40 / 3)
                                                        + (1 - e_nd_c_b_na) * (f_ne_nd_c_b_na * (40 * b_na + 40 * f_ne_nd_c_b_na + 60 / 3)
                                                                               + (1 - f_ne_nd_c_b_na) * (80 * b_na + 40))))
                        - 80 * c_b_na * c_b_na)\
    + (1 - a) * (1 - b_na) * (-20 * (1 - c_nb_na)
                              + c_nb_na * (d_c_nb_na * (e_d_c_nb_na * (40 * d_c_nb_na + 40 * e_d_c_nb_na + 40 / 3)
                                                        + (1 - e_d_c_nb_na) * (f_ne_d_c_nb_na * (40 * d_c_nb_na + 40 * f_ne_d_c_nb_na + 60 / 3)
                                                                               + (1 - f_ne_d_c_nb_na) * (80 * d_c_nb_na + 40)))
                                           + (1 - d_c_nb_na) * (e_nd_c_nb_na * (f_e_nd_c_nb_na * (40 * e_nd_c_nb_na + 40 * f_e_nd_c_nb_na + 60 / 3)
                                                                                + (1 - f_e_nd_c_nb_na) * (80 * e_nd_c_nb_na + 40))
                                                                + (1 - e_nd_c_nb_na) * (f_ne_nd_c_nb_na * (80 * f_ne_nd_c_nb_na + 40)
                                                                                        + (1 - f_ne_nd_c_nb_na) * 100)))
                              - 80 * c_nb_na * c_nb_na * (1 - (1 - d_c_nb_na) * (1 - e_nd_c_nb_na) * (1 - f_ne_nd_c_nb_na)))
evd = a * b_a * c_b_a * 0\
    + a * b_a * (1 - c_b_a) * (-20 * (1 - d_nc_b_a)
                               + d_nc_b_a * (40 * a + 40 * b_a + 20 / 3)
                               - 80 * d_nc_b_a * d_nc_b_a)\
    + a * (1 - b_a) * c_nb_a * (-20 * (1 - d_c_nb_a)
                                + d_c_nb_a *
                                (40 * a + 40 *
                                 c_nb_a+20/3)
                                - 80 * d_c_nb_a * d_c_nb_a)\
    + a * (1 - b_a) * (1 - c_nb_a) * (-20 * (1 - d_nc_nb_a)
                                      + d_nc_nb_a * (e_d_nc_nb_a * (40 * a + 40 * e_d_nc_nb_a + 40 / 3)
                                                     + (1 - e_d_nc_nb_a) * (f_ne_d_nc_nb_a * (40 * a + 40 * f_ne_d_nc_nb_a + 60 / 3)
                                                                            + (1 - f_ne_d_nc_nb_a) * (80 * a + 40)))
                                      - 80 * d_nc_nb_a * d_nc_nb_a)\
    + (1 - a) * b_na * c_b_na * (-20 * (1 - d_c_b_na)
                                 + d_c_b_na *
                                 (40 * b_na + 40 * c_b_na+20/3)
                                 - 80 * d_c_b_na * d_c_b_na)\
    + (1 - a) * b_na * (1 - c_b_na) * (-20 * (1 - d_nc_b_na)
                                       + d_nc_b_na * (e_d_nc_b_na * (40 * b_na + 40 * e_d_nc_b_na + 40 / 3)
                                                      + (1 - e_d_nc_b_na) * (f_ne_d_nc_b_na * (40 * b_na + 40 * f_ne_d_nc_b_na + 60 / 3)
                                                                             + (1 - f_ne_d_nc_b_na) * (80 * b_na + 40)))
                                       - 80 * d_nc_b_na * d_nc_b_na)\
    + (1 - a) * (1 - b_na) * c_nb_na * (-20 * (1 - d_c_nb_na)
                                        + d_c_nb_na * (e_d_c_nb_na * (40 * c_nb_na + 40 * e_d_c_nb_na + 40 / 3)
                                                       + (1 - e_d_c_nb_na) * ((f_ne_d_c_nb_na) * (40 * c_nb_na + 40 * f_ne_d_c_nb_na + 60 / 3)
                                                                              + (1 - f_ne_d_c_nb_na) * (80 * c_nb_na + 40)))
                                        - 80 * d_c_nb_na * d_c_nb_na)\
    + (1 - a) * (1 - b_na) * (1 - c_nb_na) * (-20 * (1 - d_nc_nb_na)
                                              + d_nc_nb_na * (e_d_nc_nb_na * (f_e_d_nc_nb_na * (40 * e_d_nc_nb_na + 40 * f_e_d_nc_nb_na + 60 / 3)
                                                                              + (1 - f_e_d_nc_nb_na) * (80 * e_d_nc_nb_na + 40))
                                                              + (1 - e_d_nc_nb_na) * (f_ne_d_nc_nb_na * (80 * f_ne_d_nc_nb_na + 40)
                                                                                      + (1 - f_ne_d_nc_nb_na) * 100))
                                              - 80*d_nc_nb_na*d_nc_nb_na*(e_d_nc_nb_na + (1 - e_d_nc_nb_na) * f_ne_d_nc_nb_na))
eve = a * b_a * c_b_a * 0\
    + a * b_a * (1 - c_b_a) * d_nc_b_a * 0\
    + a * b_a * (1 - c_b_a) * (1-d_nc_b_a) * (-20*(1-e_nd_nc_b_a) +
                                              e_nd_nc_b_a * (40 * a + 40 * b_a + 40 / 3) - 80 * e_nd_nc_b_a * e_nd_nc_b_a)\
    + a * (1 - b_a) * c_nb_a * d_c_nb_a * 0\
    + a * (1 - b_a) * c_nb_a * (1-d_c_nb_a) * \
    (-20 * (1 - e_nd_c_nb_a) + e_nd_c_nb_a * (40 * a + 40 * c_nb_a + 40 / 3) - 80 * e_nd_c_nb_a * e_nd_c_nb_a)\
    + a * (1 - b_a) * (1-c_nb_a) * d_nc_nb_a * \
    (-20 * (1 - e_d_nc_nb_a) + e_d_nc_nb_a * (40 * a + 40 * d_nc_nb_a + 40 / 3) - 80 * e_d_nc_nb_a * e_d_nc_nb_a)\
    + a * (1 - b_a) * (1-c_nb_a) * (1-d_nc_nb_a) * (-20*(1-e_nd_nc_nb_a)+e_nd_nc_nb_a*(f_e_nd_nc_nb_a * (40 * a + 40 * f_e_nd_nc_nb_a + 60 / 3)
                                                                                       + (1 - f_e_nd_nc_nb_a) * (80 * a + 40)) - 80 * e_nd_nc_nb_a * e_nd_nc_nb_a)\
    + (1 - a) * b_na * c_b_na * d_c_b_na * 0\
    + (1 - a) * b_na * c_b_na * (1-d_c_b_na) * \
    (-20 * (1 - e_nd_c_b_na) + e_nd_c_b_na * (40 * b_na + 40 * c_b_na + 40 / 3) - 80 * e_nd_c_b_na * e_nd_c_b_na)\
    + (1 - a) * b_na * (1-c_b_na) * d_nc_b_na * \
    (-20 * (1 - e_d_nc_b_na) + e_d_nc_b_na * (40 * b_na + 40 * d_nc_b_na + 40 / 3) - 80 * e_d_nc_b_na * e_d_nc_b_na)\
    + (1 - a) * b_na * (1 - c_b_na) * (1 - d_nc_b_na) * (-20 * (1 - e_nd_nc_b_na)+e_nd_nc_b_na*(f_e_nd_nc_b_na * (40 * b_na + 40 * f_e_nd_nc_b_na + 60 / 3)
                                                                                                + (1 - f_e_nd_nc_b_na) * (80 * b_na + 40)) - 80 * e_nd_nc_b_na * e_nd_nc_b_na)\
    + (1 - a) * (1-b_na) * c_nb_na * d_c_nb_na * \
    (-20 * (1 - e_d_c_nb_na) + e_d_c_nb_na * (40 * c_nb_na + 40 * d_c_nb_na + 40 / 3) - 80 * e_d_c_nb_na * e_d_c_nb_na)\
    + (1 - a) * (1-b_na) * c_nb_na * (1-d_c_nb_na) * (-20*(1-e_nd_c_nb_na)+e_nd_c_nb_na*(f_e_nd_c_nb_na * (40 * c_nb_na + 40 * f_e_nd_c_nb_na + 60 / 3)
                                                                                         + (1 - f_e_nd_c_nb_na) * (80 * c_nb_na + 40)) - 80 * e_nd_c_nb_na * e_nd_c_nb_na)\
    + (1 - a) * (1-b_na) * (1-c_nb_na) * d_nc_nb_na * (-20*(1-e_d_nc_nb_na)+e_d_nc_nb_na*(f_e_d_nc_nb_na * (40 * d_nc_nb_na + 40 * f_e_d_nc_nb_na + 60 / 3)
                                                                                          + (1 - f_e_d_nc_nb_na) * (80 * d_nc_nb_na + 40)) - 80 * e_d_nc_nb_na * e_d_nc_nb_na)\
    + (1 - a) * (1-b_na) * (1-c_nb_na) * (1-d_nc_nb_na) * (-20*(1-e_nd_nc_nb_na)+e_nd_nc_nb_na*(f_e_nd_nc_nb_na * (80 * f_e_nd_nc_nb_na + 40)
                                                                                                + (1 - f_e_nd_nc_nb_na) * 100)-80*e_nd_nc_nb_na*e_nd_nc_nb_na*(f_e_nd_nc_nb_na))
evf = -eva - evb - evc - evd - eve
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
print("evd=", evd)
print("eve=", eve)
print("evf=", evf)
