#building histoograms on just python
a = (0,1,1,1,2,3,7,7,23)
def count_elements(seq) -> dict:
    """""Tally elements from `seq`"""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i,0) + 1
    return hist
#count the number of each element in the sequence
counted = count_elements(a)

from collections import Counter
#do the same as above but with collection.counter and not function
recount = Counter(a)

#hist before the loop
def ascii_histogram(seq) -> None:
    """""a horizontal frq table """
    counted = count_elements(seq)
    for k in sorted(counted):
     print('{0:5d} {}'.format(k,'+'* counted[k]))
#clarify#

import  random
random.seed(1)

vals = [1,3,4,6,8,9,10]
#each number in vals will occur between 5 and 15 times
freq = (random.randint(5,15) for _ in vals)
data = []
for f,v in zip(freq, vals):
    data.extend([v] * f)
ascii_histogram(data)

#now use numpy
import numpy as np
np.random.seed(444)
np.set_printoptions(precision = 3)

d = np.random.laplace(loc=15, scale=3, size=500)
hist, bin_edges = np.histogram(d)

first_edge, last_edge = a.min(), a.max()
n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge, num=n_equal_bins+1, endpoint=True)

#using matplotlib

import matplotlib.pyplot as plt
n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)

