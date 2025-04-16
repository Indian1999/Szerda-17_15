import random

TARGET = "Ez itt a genetikus algoritmus"
POPULATION_SIZE = 100
MUTATION_RATE = 0.01 # Egy egyed egy karaktere ennyi eséllyel mutálódik
GENERATIONS = 1000
CHARS = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyzAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ .,?!"

def random_egyed():
    egyed = ""
    while len(egyed) != len(TARGET):
        egyed += random.choice(CHARS)
    return egyed

def fitness(egyed):
    fitness_score = 0
    for i in len(egyed):
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

def genetic_algorithm():
    population = [random_egyed() for i in range(POPULATION_SIZE)]
    
genetic_algorithm()