# -*- coding: cp1251 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy, scipy.stats

print("started plotting")

file = open("experiments/uniformdistr.txt")
file1 = open("experiments/ConstN.txt")
file2 = open("experiments/small1.txt")
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

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
X1 = np.array(X1)
Y1 = np.array(Y1)
fig,(ax,ax1) = plt.subplots(ncols=2, constrained_layout=False)
for i in range(len(X)):
    ax.plot(Z[i]*np.ones(len(X[i])),X[i],marker = '.')

ax.grid()
ax.set(xlabel='x: number of digits I', ylabel='y: number of operations')

for i in range(len(X)//64):
    ax.text(65,X[-1-i][0],str(str(16-i)+'*10^4'))

for i in range(16):
    line = np.polyfit(np.repeat(Z[i::16],50),np.ndarray.flatten(X[i::16][:]),1)
    ax.plot([0,65],[line[1],line[0]*65+line[1]],color = 'black', alpha = 0.5, linestyle = '--')

for i in range(len(X)):
    ax1.plot(Y[i]*np.ones(len(X[i])),X[i],marker = '.')

ax1.grid()
ax1.set(xlabel='x: array length N', ylabel='y: number of operations')

for i in range(64):
    ax1.text(163000,X[(i*16+15)][0],str(i+1))

for i in range(64):
    line = np.polyfit(np.repeat(Y[0:16],50),np.ndarray.flatten(X[i*16:(i*16+16)][:]),1)
    ax1.plot([0,160000],[line[1],line[0]*160000+line[1]],color = 'black', alpha = 0.5, linestyle = '--')

fig.suptitle('number of binary digits I = 1:64, array length N = 10^4:16*10^4, number of repeated tests with same array length and digits = 50', fontsize=16)
plt.show()

fig,ax = plt.subplots()
A = np.sort(X1[0])
pmf = scipy.stats.binom.pmf(A-64*(6*10**6+4),64000000,0.5)
ax.plot(A,pmf)
ax.hist(A,100,normed=True)
ax.set(xlabel='x: number of operations N', ylabel='distribution',
    title='distribution of number of operations. number of digits I = 64, array length N = 10^6, number of tests M = 10^4')
plt.show()



fig,ax = plt.subplots()

X, Y, Z = [],[],[]
for line in file2:
  l = [int(s) for s in line.split()]
  Y.append(l[0])
  Z.append(l[1])
  X.append(l[2:])

for i in range(len(X)):
    ax.plot(Y[i]*np.ones(len(X[i])),X[i],marker = '.')

ax.grid()
ax.set(xlabel='x: number of elements n', ylabel='y: number of operations')
fig.suptitle('number of operations on small sets. n = 10 to 1000, m = 64, 10000 repeats')
X = np.array(X)
line = np.polyfit(np.repeat(Y[:],10000),np.ndarray.flatten(X[:][:]),1)
ax.plot([0,1000],[line[1],line[0]*1000+line[1]],color = 'black', alpha = 0.5, linestyle = '--')

plt.show()

fig,ax = plt.subplots()
A = np.sort(X[-1])
pmf = scipy.stats.binom.pmf(A-64*(6*1000+4),64000,0.5)
ax.plot(A,pmf)
ax.hist(A,100,normed=True)
ax.set(xlabel='x: number of operations N', ylabel='y: distribution')
fig.suptitle('distribution n = 1000, m = 64, 10000 repeats')

plt.show()

file.close()
