import numpy as np

a = np.array ([0,1,2,3,4])

b = np.array([[1,2,3], [4,5,6]])
c = np.array([[[1], [2]],[[1], [2]]])

d = np.linspace(0,1,6)
e = np.linspace(0,1,5, endpoint = False)
f = np.diag(np.array([1,2,3,4]))

g =  np.random.rand(4) # uniform in [0,1]
h = np.random.randn(4) # gaussian

i = np.random.seed(1234)  #setting the random seed
print (i)


# pest

t = np.zeros((2,3))
o = np.arange(0,9)#


np.eye(3)

np.diag(np.array([1,2,3]))

np.empty((3,3))

#data types

a.dtype
h.dtype
d.dtype

#which data do you want





a_ = np.array([4+5j, 3+4j, 4+7j])
a_.dtype







