# PSO (Particle Swarm Optimization) [Részecske Raj Optimalizáció]
import numpy as np # pip install numpy

# Termékek:     A    B    C    D     E    F 
# Eladási ár:   5    6    7    5     6    7
# erőforrás 1:  2    3    2    1     1    3       [1050] limit
# erőforrás 2:  2    1    3    1     3    2       [1050] limit
# erőforrás 3:  1    2    1    4     1    2       [1080] limit

# Mely termékekből mennyit gyártsunk, hogy a lehető legtöbb pénzünk legyen?

# A feladat paramétereinek definiálása
n_products = 6

resource_limits = np.array([1050, 1050, 1080])
revenues = np.array([5,6,7,5,6,7])
machine_hours = np.array([2,3,2,1,1,3])
labor_hours = np.array([2,1,3,1,3,2])
energy = np.array([1,2,1,4,1,2])

# A részecske raj paraméterei
n_particles = 50
max_iter = 100
w = 0.9 # inercia súly
c1 = 4 # Gyorsulási eggyütható
c2 = 4 # Gyorsulási eggyütható

# Részecskék létrehozása
# 1 részecske - a 6 különböző termékből, hány darabot gyártsunk (számhatos)
# 1 részecske sebesség 6 számmal írható le (vektor6)
particles = np.random.randint(0, 300, size = (n_particles, n_products))
velocities = np.zeros((n_particles, n_products)) # 50*6 os mátrix tele 0-kal

# Korlátozzuk a termékek lehetséges számát
lower_bounds = np.zeros(n_products)
upper_bounds = resource_limits[0] // machine_hours

# Legjobb pozíciók inicializálása
pbest = np.copy(particles)
pbest_scores = np.array([-np.inf] * n_particles)
gbest = particles[0]
gbest_score = -np.inf

def evaluate(particle):
    if np.sum(particle * machine_hours) > resource_limits[0]:
        return -np.inf
    if np.sum(particle * labor_hours) > resource_limits[1]:
        return -np.inf
    if np.sum(particle * energy) > resource_limits[2]:
        return -np.inf
    return np.sum(particle * revenues)
    