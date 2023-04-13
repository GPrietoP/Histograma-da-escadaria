# Jogo de dados para subir escadas. Se o dado cair 1,2, descemos um degrau. Se cair 3, 4, 5 subimos 1 degrau

# Import
import numpy as np
from matplotlib import pyplot as plt

# Simulando 100 vezes
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
f1 = plt.figure(1)
plt.plot(np_aw_t)
f1.show()

# Ultima linha
ends = np_aw_t[-1,:]

# Plotando histogramas
f2 = plt.figure(2)
plt.hist(ends)
f2.show()

input()