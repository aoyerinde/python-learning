import pandas as pd
import numpy as np


data = pd.DataFrame({
    'Days':['Monday', 'Tuesday','Wednesday','Thursday'],
    'Months': ['Jan','feb','mar', np.nan]
})


b = np.zeros((4,3))
i = np.eye(3)
d = np.arange(1,10).reshape(3,3)
print (d)

#multiply

M = np.dot(i,d)

#sum elements

sum_val = np.sum(M)

#along rows sum

sum_row = np.sum(M,axis = 1)

rand_ = np.random.rand(2,3)

rand_step = np.random.rand(5,15)


a = np.arange(5,15,2)

#extend a

a = np.append(a, 19)

#extend a by exact value

a = np.append(a, [21,23,25])

#find diff in array

A =  np.diff(a, n=1)

B =  np.diff(A, n=1)

#find double difference

C = np.diff(A, n=2)

#define 3 lists

e = [1,2,3]
f = [4,5,6]
g = [7,8,9]

h = np.stack((e,f,g))

l = np.column_stack(h)

temp = a[2:5]

# creat e an empty array and put A in K
K = np.array([])
for  e in  a: K = np.append(K, e+1)
