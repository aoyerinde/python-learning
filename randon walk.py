import numpy as np
import matplotlib.pyplot as plt

# 1000 iterations with 200 steps each

n_stories = 1000
t_max = 200

t = np.arange(t_max)

#steps can be -1 or 1

steps = 2 * np.random.randint(0, 1+1, (n_stories,t_max)) - 1

#

positions = np.cumsum(steps, axis=1)

#time evolution of mean square distance

sq_distance = positions**2
mean_sq_distance = np.mean(sq_distance, axis=0)

#plot distance d from origin as a funtion


plt.figure(figsize=(4,3))
plt.plot(t,np.sqrt(mean_sq_distance),'g.',t,np.sqrt(t),'y-')
plt.xlabel(r"$t$")
plt.ylabel(r"$\sqrt{\langle(\delta x^2)}$")
plt.tight_layout()
plt.show()

