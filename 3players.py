import matplotlib.pyplot as plt
# バグあり
a = 0.5
b_a = 0.5
b_na = 0.5
c_b_a = 0.5
c_b_na = 0.5
c_nb_a = 0.5
a_results = []
b_a_results = []
b_na_results = []
c_b_a_results = []
c_b_na_results = []
c_nb_a_results = []
for i in range(1000):
    a = (60 + 80 * b_a * b_a - 30 * b_a+c_b_a*(-40*b_a*b_a-10*b_a)+40*c_b_a*c_b_a*b_a+c_nb_a *
         (-30+30*b_a)+80*c_nb_a*c_nb_a*(1-b_a))/(160 * b_a - 80 * b_a*c_b_a - c_nb_a * (-160 + 80 * b_a))
    a_results.append(a)
    b_a = (30-40*c_b_a*a+80*a - 10*c_b_a+40*c_b_a*c_b_a)/160
    b_a_results.append(b_a)
    c_b_a = (2 * a + 2 * b_a + 1) / 8
    c_b_a_results.append(c_b_a)
    c_nb_a = (8 * a + 3) / 16
    c_nb_a_results.append(c_nb_a)
    b_na = (6-3*c_b_na+8*c_b_na*c_b_na)/(16*c_b_na)
    b_na_results.append(b_na)
    c_b_na = (8 * b_na + 3) / 16
    c_b_na_results.append(c_b_na)
plt.plot(a_results)
plt.show()
plt.plot(b_a_results)
plt.show()
plt.plot(c_b_a_results)
plt.show()
plt.plot(c_nb_a_results)
plt.show()
plt.plot(b_na_results)
plt.show()
plt.plot(c_b_na_results)
plt.show()
print("a=", a)
print("b_a=", b_a)
print("c_b_a=", c_b_a)
print("c_nb_a=", c_nb_a)
print("b_na=", b_na)
print("c_b_na=", c_b_na)
eva = -20 * (1 - a) + a * (b_a * (c_b_a * (40*b_a+40*c_b_a-80*a)+(1-c_b_a)
                                  * (80*b_a-80*a+10))+(1-b_a)*(c_nb_a*(80*c_nb_a-80*a+10)+(1-c_nb_a)*40))
evb = a * (b_a*(c_b_a*(40*a+40*c_b_a-80*b_a)+(1-c_b_a)*(80*a-80*b_a+10))-20 *
           (1-b_a))+(1-a)*(b_na*(c_b_na*(80*c_b_na-80*b_na+10)+(1-c_b_na)*40)-20*(1-b_na))
evc = -eva - evb
print("eva=", eva)
print("evb=", evb)
print("evc=", evc)
