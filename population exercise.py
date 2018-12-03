import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('C:/Users/Serkan/PycharmProjects/panda/scipy-lecture-notes-2017.1.1/data/populations.txt')

year, hares, lynxes, carrots = data.T

plt.axes ([0.2,0.1,0.5,0.8])
plt.plot (year, hares, year,  lynxes, year, carrots)
plt.legend(('hares', 'lynxes', 'carrots'), loc= (1.05, 0.5))

plt.show()
