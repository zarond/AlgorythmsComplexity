# -*- coding: cp1251 -*-

import numpy as np
import matplotlib.pyplot as plt

print("started plotting")

file = open("experiments/uniformdistr.txt")
file1 = open("experiments/ConstN.txt")
#fileskip = open("outskips.txt")

X, Y, Z = [],[],[]
for line in file:
  l = [int(s) for s in line.split()]
  Y.append(l[0])
  Z.append(l[1])
  X.append(l[2:])

X1, Y1 = [],[]
for line in file1:
  l = [int(s) for s in line.split()]
  Y1.append(l[0])
  X1.append(l[2:])


fig,(ax,ax1) = plt.subplots(ncols=2, constrained_layout=False)
for i in range(len(X)):
    ax.plot(Z[i]*np.ones(len(X[i])),X[i],marker = '.')

ax.grid()
ax.set(xlabel='x: number of digits I', ylabel='y: number of operations')

#np.polyfit(X[0:64])

for i in range(len(X)):
    ax1.plot(Y[i]*np.ones(len(X[i])),X[i],marker = '.')

ax1.grid()
ax1.set(xlabel='x: array length N', ylabel='y: number of operations')

fig.suptitle('number of binary digits I = 1:64, array length N = 10^4:16*10^4, number of repeated tests with same array length and digits = 50', fontsize=16)
plt.show()


fig,ax = plt.subplots()
ax.hist(X1[0],100)
ax.set(xlabel='x: number of operations N', ylabel='distribution',
    title='distribution of number of operations. number of digits I = 64, array length N = 10^6, number of tests M = 10^4')
plt.show()


fig,ax = plt.subplots()

file.close()
