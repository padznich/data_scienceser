
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import fsolve

data = sp.genfromtxt("/home/padznich/code/neural/web_traffic/web_traffic.tsv", delimiter=",")

x = data[:, 0]
y = data[:, 1]

# remove nan values
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


def error(f, x, y):
    return sp.sum((f(x)-y)**2)


fp1 = sp.polyfit(x, y, 1)
f1 = sp.poly1d(fp1)

fp2 = sp.polyfit(x, y, 2)
f2 = sp.poly1d(fp2)

fp3 = sp.polyfit(x, y, 3)
f3 = sp.poly1d(fp3)


plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
# plt.autoscale(tight=True)

fx = sp.linspace(0, x[-1], 1000)  # generate X-values for plotting

plt.scatter(x, y,  color='c')
plt.plot(fx, f1(fx), linewidth=3)
plt.plot(fx, f2(fx), linewidth=3)
plt.plot(fx, f3(fx), linewidth=3)


print('d=1 Error: ', error(f1, x, y))
print('d=2 Error: ', error(f2, x, y))
print('d=3 Error: ', error(f3, x, y))


reached_min = fsolve(f3 - 10000, 1000) / (7 * 24)
print(f3)
print("10,000 hits/hour expected at week %f" % reached_min[0])


plt.legend(["d=%i" % f1.order, "d=%i" % f2.order, "d=%i" % f3.order], loc="upper right")
plt.grid()
plt.show()
