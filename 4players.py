import matplotlib.pyplot as plt
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

a_results = []
b_a_results = []
c_b_a_results = []
d_nc_b_a_results = []
c_nb_a_results = []
d_c_nb_a_results = []
d_nc_nb_a_results = []
b_na_results = []
c_b_na_results = []
d_c_b_na_results = []
d_nc_b_na_results = []
c_nb_na_results = []
d_c_nb_na_results = []
for i in range(1000):
    a = (20+b_a*(c_b_a*(40*b_a+40*c_b_a)+(1-c_b_a)*(d_nc_b_a *
                                                    (40 * b_a + 40 * d_nc_b_a + 20 / 3) + (1 - d_nc_b_a) * (80 * b_a + 20))) + (1 - b_a) * (c_nb_a * (d_c_nb_a * (40 * c_nb_a + 40 * d_c_nb_a + 20 / 3) + (1 - d_c_nb_a) * (80 * c_nb_a + 20)) + (1 - c_nb_a) * (d_nc_nb_a * (80 * d_nc_nb_a + 20) + (1 - d_nc_nb_a) * 60))) / (160 * (1 - (1 - b_a) * (1-c_nb_a) * (1 - d_nc_nb_a)))
    b_a = (20+c_b_a*(40*a+40*c_b_a)+(1-c_b_a)*((d_nc_b_a) *
                                               (40 * a + 40 * d_nc_b_a + 20 / 3) + (1 - d_nc_b_a) * (80 * a + 20))) / 160
    c_b_a = (20 + 40 * a + 40 * b_a) / 160
    d_nc_b_a = (20 + 40 * a + 40 * b_a + 20 / 3) / 160
    c_nb_a = (20 + d_c_nb_a * (40 * a + 40 * d_c_nb_a + 20 / 3) +
              (1 - d_c_nb_a) * (80 * a + 20)) / 160
    d_c_nb_a = (20 + 40 * a + 40 * c_nb_a + 20 / 3) / 160
    d_nc_nb_a = (20 + 80 * a + 20) / 160
    b_na = (20 + c_b_na * (d_c_b_na * (40 * c_b_na + 40 * d_c_b_na + 20 / 3) + (1-d_c_b_na) * (80*c_b_na+20)) + (1 - c_b_na) * (d_nc_b_na *
                                                                                                                                (80 * d_nc_b_na + 20) + (1 - d_nc_b_na) * 60)) / (160 * (c_b_na + (1 - c_b_na) * d_nc_b_na))
    c_b_na = (20 + d_c_b_na * (40 * b_na + 40 * d_c_b_na + 20 / 3) +
              (1 - d_c_b_na) * (80 * b_na + 20)) / 160
    d_c_b_na = (20 + 40 * b_na + 40 * c_b_na + 20 / 3) / 160
    d_nc_b_na = (20 + 80 * b_na + 20) / 160
    c_nb_na = (20 + d_c_nb_na * (80 * d_c_nb_na + 20) +
               (1 - d_c_nb_na) * 60) / (160 * d_c_nb_na)
    d_c_nb_na = (20+80*c_nb_na+20)/160

    a_results.append(a)
    b_a_results.append(b_a)
    c_b_a_results.append(c_b_a)
    d_nc_b_a_results.append(d_nc_b_a)
    c_nb_a_results.append(c_nb_a)
    d_c_nb_a_results.append(d_c_nb_a)
    d_nc_nb_a_results.append(d_nc_nb_a)
    b_na_results.append(b_na)
    c_b_na_results.append(c_b_na)
    d_c_b_na_results.append(d_c_b_na)
    d_nc_b_na_results.append(d_nc_b_na)
    c_nb_na_results.append(c_nb_na)
    d_c_nb_na_results.append(d_c_nb_na)


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
eva = -20*(1-a) + a * (b_a*(c_b_a*(40*b_a+40*c_b_a-80*a)+(1-c_b_a)*(d_nc_b_a*(40*b_a+40*d_nc_b_a-80*a+20/3)+(1-d_nc_b_a)*(80*b_a-80*a+20)))+(1-b_a) *
                       (c_nb_a*(d_c_nb_a*(40*c_nb_a+40*d_c_nb_a-80*a+20/3)+(1-d_c_nb_a)*(80*c_nb_a-80*a+20))+(1-c_nb_a)*(d_nc_nb_a*(80*d_nc_nb_a-80*a+20)+(1-d_nc_nb_a)*60)))
evb = a * (b_a*(c_b_a*(40*a+40*c_b_a-80*b_a)+(1-c_b_a)*(d_nc_b_a*(40*a+40*d_nc_b_a-80*b_a+20/3)+(1-d_nc_b_a)*(80*a-80*b_a+20)))+(1-b_a)*(-20)) + (1-a) * (-20*(1-b_na) +
                                                                                                                                                          b_na*(c_b_na*(d_c_b_na*(40*c_b_na+40*d_c_b_na-80*b_na+20/3)+(1-d_c_b_na)*(80*c_b_na-80*b_na+20))+(1-c_b_na)*(d_nc_b_na*(80*d_nc_b_na-80*b_na+20)+(1-d_nc_b_na)*(60))))
evc = a * (b_a * ((-20) * (1 - c_b_a) + c_b_a *
                  (40 * a + 40 * b_a - 80 * c_b_a)) + (1 - b_a) * ((-20) * (1 - c_nb_a) + c_nb_a * (d_c_nb_a * (40 * a + 40 * d_c_nb_a - 80 * c_nb_a + 20 / 3) + (1 - d_c_nb_a) * (80 * a - 80 * c_nb_a + 20)))) + (1-a) * (b_na*(-20*(1-c_b_na)+c_b_na*(d_c_b_na*(40*b_na+40*d_c_b_na-80*c_b_na+20/3)+(1-d_c_b_na)*(80*b_na-80 * c_b_na+20))+(1-b_na) * (-20*(1-c_nb_na)+c_nb_na*(d_c_nb_na * (80*d_c_nb_na-80*c_nb_na+20)+(1-d_c_nb_na)*(60)))))
evd = -eva - evb - evc
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
print("evd=", evd)
