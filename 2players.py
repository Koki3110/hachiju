import matplotlib.pyplot as plt
a = 0.5
b = 0.5
aresults = []
bresults = []
for i in range(1000):
    a = (4 * b * b - b + 2)/(8 * b)
    aresults.append(a)
    b = (4 * a + 1)/8
    bresults.append(b)
plt.plot(aresults)
plt.show()
plt.plot(bresults)
plt.show()
print("a=", a)
print("b=", b)
eva = -20 * (1 - a) + a * (b * 80 * (b - a) + 20 * (1 - b))
evb = -eva
print("eva=", eva)
print("evb=", evb)
