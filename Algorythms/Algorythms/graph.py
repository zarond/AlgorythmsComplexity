import numpy as np
import matplotlib.pyplot as plt

print("started plotting")

file = open("out.txt")
#fileskip = open("outskips.txt")

X, Y = [],[]
for line in file:
  l = [float(s) for s in line.split()]
  Y.append(l[0])
  X.append(l[2:])

for i in range(len(X)):
    #plt.plot(Y[i]*np.ones(len(X[i])),X[i],marker = '.')
    pass

plt.hist(X[0],100)
plt.show()

file.close()
