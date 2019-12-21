# -*- coding: cp1251 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy, scipy.stats

print("started plotting")

file = open("experiments/uniformdistr.txt")
file1 = open("experiments/double11.txt")
file2 = open("experiments/double12.txt")
#fileskip = open("outskips.txt")

X1, X2, Z = [],[],[]
for line in file1:
  l = [int(s) for s in line.split()]
  X1.append(l[2:])
  Z.append(l[0])

for line in file2:
  l = [int(s) for s in line.split()]
  X2.append(l[2:])

X1 = np.array(X1)
X2 = np.array(X2)
X1 = np.mean(X1,axis = 1)
X2 = np.mean(X2,axis = 1)
Z = np.array(Z)

Y = X2/X1

fig,ax = plt.subplots()
ax.grid()
ax.set(xlabel='x: N - length of array, from 10^3 to 10^6 with 10^3 step. 5 repeats for each N', ylabel='y: T(2n)/T(n)')
fig.suptitle('T(2n)/T(n)')
ax.plot(Z,Y)
plt.show()

