import numpy as np

i = 10
print(type(i))

a_i = np.zeros(i, dtype=int)
print (type(a_i))
print(type(a_i[0]))
#why is it int32 instead of int64?
#what happens if you use ones instead of zeros?

x = 119.0
print(type(x))

y = 1.19e2
print(type(y))

z = np.zeros(i, dtype=float)
print(type(z))
print(type(z[0]))

d = np.zeros((2,2), dtype=float)
d [0,0] = 1.0
d [1,1] = 1.0
print(d)