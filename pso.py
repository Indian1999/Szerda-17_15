# PSO (Particle Swarm Optimization) [Részecske Raj Optimalizáció]
import numpy as np # pip install numpy

# Termékek:     A    B    C    D     E    F 
# Eladási ár:   5    6    7    5     6    7
# erőforrás 1:  2    3    2    1     1    3       [1050] limit
# erőforrás 2:  2    1    3    1     3    2       [1050] limit
# erőforrás 3:  1    2    1    4     1    2       [1080] limit

# Mely termékekből mennyit gyártsunk, hogy a lehető legtöbb pénzünk legyen?

n_products = 6

resource_limits = np.array([1050, 1050, 1080])
revenues = np.array([5,6,7,5,6,7])
machine_hours = np.array([2,3,2,1,1,3])
labor_hours = np.array([2,1,3,1,3,2])
energy = np.array([1,2,1,4,1,2])
