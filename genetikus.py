import random

TARGET = "Ez itt a genetikus algoritmus"
POPULATION_SIZE = 100
MUTATION_RATE = 0.01 # Egy egyed egy karaktere ennyi eséllyel mutálódik
GENERATIONS = 1000
CHARS = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyzAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ .,?!"

def write_population_to_file(population, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for egyed in population:
            f.write(egyed + "\n")
            
def random_egyed():
    egyed = ""
    while len(egyed) != len(TARGET):
        egyed += random.choice(CHARS)
    return egyed

def fitness(egyed):
    fitness_score = 0
    for i in range(len(egyed)):
        if egyed[i] == TARGET[i]:
            fitness_score += 1
    return fitness_score

def keresztezés(szülő1, szülő2):
    index = random.randint(1, len(szülő1) - 2)
    gyerek = szülő1[:index] + szülő2[index:]
    return gyerek

def mutáció(egyed):
    mutált_egyed = ""
    for char in egyed:
        if random.random() < MUTATION_RATE:
            mutált_egyed += random.choice(CHARS)
        else:
            mutált_egyed += char
    return mutált_egyed
            
def selection(population, n = 5):
    """
    Kiválaszt a populációból 5 egyedet, ezek közül a legjobbat visszaadja
    """
    egyedek = random.choices(population, k = n)
    return max(egyedek, key=fitness)
    

def genetic_algorithm():
    population = [random_egyed() for i in range(POPULATION_SIZE)]
    
    for generation in range(GENERATIONS):
        best = population[0]
        for egyed in population:
            if fitness(egyed) > fitness(best):
                best = egyed
        print(f"Generation {generation}: {best} (Fitness: {fitness(best)})")
        
        if best == TARGET:
            print("Optimal solution found!")
            break
        
        new_population = [best]
        while len(new_population) != POPULATION_SIZE:
            child = keresztezés(selection(population), selection(population))
            child = mutáció(child)
            new_population.append(child)
            
        population = new_population[:]
    
genetic_algorithm()